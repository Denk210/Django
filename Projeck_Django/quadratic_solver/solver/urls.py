from django.urls import path
from . import views

urlpatterns = [
    path('solve/', views.solve_quadratic, name='solve_quadratic'),
    path('trinager/', views.quadratic_trainer, name='quadratic_trainer'),
]