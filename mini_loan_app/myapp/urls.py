from django.urls import path
from . import views

urlpatterns = [
    path('bfhl', views.BFHLView.as_view(), name='bfhl'),
    path('', views.bajaj_frontend_view, name='bajaj_frontend'),
]
