from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('workout/', views.workout, name='workout'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('disease/', views.disease, name='disease')
]
