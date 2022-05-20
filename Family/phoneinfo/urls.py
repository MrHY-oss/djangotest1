from rest_framework.routers import DefaultRouter,SimpleRouter
from . import views

#
from django.urls import path


router = DefaultRouter()
# router = SimpleRouter()
router.register("phoneinfo",views.PhoneinfoModelViewSet,basename="phoneinfo")
# router.register("phoneinfo",views.PhoneinfoModelViewSet,basename="phoneinfo")
# router.register(r'phoneinfo/lastdata/', views.PhoneinfoModelViewSet,basename="phoneinfo")
urlpatterns = [
    path('phoneinfo/lastdata/<int:pk>/', views.PhoneinfoModelViewSet.as_view({'get': 'lastdata'}))
] + router.urls