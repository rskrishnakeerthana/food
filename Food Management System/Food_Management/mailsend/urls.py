from django.urls import path
from . import views

urlpatterns = [
    path('emailsend/',views.EmailSend,name='emailsend'),
]