from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # /plants/
    path('<int:plant_id>/', views.detail, name='detail'),  # /plants/5/
    path('<int:plant_id>/propogations/', views.propogations, name='propogations'),  # /plants/5/propogations/
    path('<int:plant_id>/propogate/', views.propogate, name='propogate'),  # /plants/5/propogate/
]
