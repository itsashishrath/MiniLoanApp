from django.urls import path
from . import views

urlpatterns = [
    path('bfhl', views.BFHLView.as_view(), name='bfhl'),
]
