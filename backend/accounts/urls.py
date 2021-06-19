from django.urls import path, include
from .views import LoginView, PasswordReset, RegistrationView, EmailView

urlpatterns = [
    path('api/accounts', include('knox.urls')),
    path('api/accounts/register', RegistrationView.as_view()),
    path('api/accounts/verifyemail', EmailView.as_view()),
    path('api/accounts/login', LoginView.as_view()),
    path('api/accounts/passwordreset', PasswordReset.as_view()),
]