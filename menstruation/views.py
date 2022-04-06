from rest_framework import status, viewsets
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

from menstruation.models import Menstruation as menstruation_model
from menstruation.utils import period_start_dates_estimate, predict_cycle_event, get_closest_date
from menstruation.serializers import MenstruationSerializer


# Create your views here.
class Menstruation(viewsets.ModelViewSet):
    queryset = menstruation_model.objects.all()
    serializer_class = MenstruationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        try:
            email = request.auth.get('email')
            user = User.objects.get(email=email)

            if self.request.user.is_authenticated:
                serializer = MenstruationSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(user=user)

                    Last_period_date = serializer.data['Last_period_date']
                    Cycle_average = serializer.data['Cycle_average']
                    Start_date = serializer.data['Cycle_average']
                    End_date = serializer.data['End_date']

                    period_dates = period_start_dates_estimate(Last_period_date,
                                                               Cycle_average,
                                                               Start_date, End_date)

                    Response({f'total_created_cycles for {user.username}': len(period_dates)},
                             status=status.HTTP_201_CREATED)
                else:
                    Response({'msg': 'Can get user'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        update_period = self.get_object()
        self.check_object_permissions(request, update_period)
        serializer = MenstruationSerializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.instance = update_period
            serializer.save()
            user_data = serializer.data
            Last_period_date = user_data.get('Last_period_date', '')
            Cycle_average = user_data.get('Cycle_average', '')
            Start_date = user_data.get('Start_date', '')
            End_date = user_data.get('End_date', '')
            period_dates = period_start_dates_estimate(Last_period_date, Cycle_average, Start_date, End_date)
            owner = request.user
            name = owner.fullname
            return Response({'name': name, 'total_created_cycles': len(period_dates)},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def cycle_event_prediction(self, request):
        event_date = self.request.query_params.get('date')

        user_data = self.get_object()
        serializer = self.serializer_class(user_data)
        Last_period_date = serializer.data.get('Last_period_date', '')
        Cycle_average = serializer.data.get('Cycle_average', '')
        Period_average = serializer.data.get('Period_average', '')
        Start_date = serializer.data.get('Start_date', '')
        End_date = serializer.data.get('End_date', '')
        date_data = get_closest_date(event_date, Last_period_date, Cycle_average, Start_date, End_date)
        try:
            last_periods = date_data[0]
            next_periods = date_data[1]
        except KeyError:
            return Response({"error": "date no in range of record available"},
                            status=status.HTTP_400_BAD_REQUEST)
        user_info = predict_cycle_event(last_periods, event_date, Cycle_average, Period_average, next_periods)

        return Response(user_info, status=status.HTTP_200_OK)
