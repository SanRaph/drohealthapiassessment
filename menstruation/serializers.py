from rest_framework import serializers
from menstruation.models import Menstruation


class MenstruationSerializer(serializers.ModelSerializer):
    Cycle_average = serializers.IntegerField(max_value=225)
    Period_average = serializers.IntegerField(min_value=1)

    class Meta:
        model = Menstruation
        fields = ['id', 'user', 'Last_period_date', 'Cycle_average', 'Period_average', 'Start_date', 'End_date']
