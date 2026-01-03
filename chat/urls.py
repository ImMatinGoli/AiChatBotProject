# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='new_chat'), # صفحه اصلی (چت جدید)
    path('<int:conversation_id>/', views.chat_view, name='conversation_detail'), # صفحه یک چت خاص
]