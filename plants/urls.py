from django.urls import path

from . import views

app_name = 'plants'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # /plants/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),  # /plants/5/
    # path('<int:plant_id>/propogations/', views.propogations, name='propogations'),  # /plants/5/propogations/
    # path('<int:plant_id>/propogate/', views.propogate, name='propogate'),  # /plants/5/propogate/
]
