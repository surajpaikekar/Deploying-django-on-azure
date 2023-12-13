from django.urls import path
from .views import SampleView

urlpatterns = [
    path('sample-view/', SampleView, name='sample-view')
]