from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('training/', views.training, name='training'),
    path('muscle/<int:muscle_id>/', views.muscle, name='muscle_id'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('disease/', views.disease, name='disease'),
    path('weight_loss/', views.weight_loss, name='weight_loss'),
]
