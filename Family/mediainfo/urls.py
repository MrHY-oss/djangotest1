from django.urls import path
from . import views

urlpatterns = [
    path('mediainfo/',views.MediainfoView.as_view()),
    path('mediaoneinfo/',views.MediainfoOneView.as_view()),
    path('mediainfo/<int:pk>/',views.MediainfoView.as_view())

]