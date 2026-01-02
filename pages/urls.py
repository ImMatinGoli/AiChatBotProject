from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('dashboard/', views.dashboard_page_view, name='dashboard'),
    path('profile/', views.profile_page_view, name='profile'),
    path('profile/update/', views.profile_update_view, name='profile_update'),
]