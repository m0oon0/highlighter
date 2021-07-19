from django.urls import path
from . import views

urlpatterns = [
    path('api/download/', views.download),
    path('api/edit/', views.edit)
]
