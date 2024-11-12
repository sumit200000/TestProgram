# spam_detection/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_spam/', views.check_spam, name='check_spam'),
]
