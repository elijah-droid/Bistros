from django.urls import path
from .views import login, signup, send_email_verification

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('send-code/', send_email_verification, name="send-email-verification")
]