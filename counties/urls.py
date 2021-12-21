from django.urls import path
from . import views

urlpatterns = [
path('counties/', views.map_view, name="map"),
]