from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name = 'SeatMonitor'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/<slug:building>/', views.detail, name='detail'),
]
