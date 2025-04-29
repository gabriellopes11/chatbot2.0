from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chatbot-response/', views.chatbot_response, name='chatbot_response'),
]
