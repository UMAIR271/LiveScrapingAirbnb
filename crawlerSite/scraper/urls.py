from django.urls import path

from . import views
#this is endpoint
urlpatterns = [
    path('', views.index, name='index'),
]