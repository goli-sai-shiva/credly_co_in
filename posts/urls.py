from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('badges/<str:badge_name>/', views.badges, name='badges'),
]