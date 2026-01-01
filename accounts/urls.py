from django.urls import path
from .views import *

urlpatterns = [
    path('logout_confirm/', LogOutConfirmView.as_view(), name='logout_confirm'),
]