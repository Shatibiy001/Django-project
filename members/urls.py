from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.members, name='members-list'),
    path('add/', views.add_member, name='add_member'),
    path('search/', views.search_view, name='search'),
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]   