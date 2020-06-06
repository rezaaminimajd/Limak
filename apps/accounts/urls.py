from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [

    path('login', view=obtain_auth_token, name='login'),
    path('signup', view=views.SignUpAPIView.as_view(), name='signup'),
    path('logout', view=views.LogoutAPIView.as_view(), name='logout'),
    path('reset-password', view=views.ResetPasswordAPIView.as_view(),
         name='reset_password'),
    path('reset-password/confirm', views.ResetPasswordConfirmAPIView.as_view(),
         name='reset-password-confirm'),
    path('change-password', view=views.ChangePasswordAPIView.as_view(),
         name='change-password')

]
