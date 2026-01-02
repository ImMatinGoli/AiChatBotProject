from django.urls import path

from . import views

urlpatterns = [
    path('logout_confirm/', views.logout_confirm_view, name='logout_confirm'),
]