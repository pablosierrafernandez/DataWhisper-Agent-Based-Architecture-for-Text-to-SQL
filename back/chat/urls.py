from django.urls import path
from .views import MessageListCreateView, APIConfigurationView, RunScriptView, ClearMessagesView

urlpatterns = [
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('configuration/', APIConfigurationView.as_view(), name='configuration'),
    path('run-script/', RunScriptView.as_view(), name='run-script'),
    path('clear-messages/', ClearMessagesView.as_view(), name='clear-messages'),  
]
