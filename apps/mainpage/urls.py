from django.urls import path
from . import views

urlpatterns = [
    path('main-page/', view=views.InformationView.as_view(),
         name='main-page')
]
