from rest_framework import routers
from menstruation import views
router = routers.DefaultRouter(trailing_slash=False)
router.register('menstruation', views.Menstruation, basename='menstruation')
urlpatterns = router.urls
