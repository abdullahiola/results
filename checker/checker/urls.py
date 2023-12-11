from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('view-results',views.results_view,name='view_results'),
]