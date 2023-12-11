from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from .models import EmailVerification
from django.contrib.auth.models import User
from Clients.models import Client
import random

def login(request):
    if request.method == 'POST':
        data = request.POST
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user:
            return redirect('dashboard')
        else:
            return redirect('.')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        data = request.POST
        email = request.POST['email']
        code = request.POST['code']
        try:
            verification = EmailVerification.objects.get(email=email)
            if int(code) == verification.code:
                if data['password'] == data['confirmpassword']:
                    user = User.objects.create(
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        email=data['email'],
                        password=make_password(data['password'])
                    )
                    client = Client.objects.create(
                        User=user
                    )
                    return redirect('login')
                else:
                    return redirect('.')
            else:
                return redirect('.')
        except EmailVerification.DoesNotExist:
            return redirect('.')
    else:
        return render(request, 'signup.html')


def send_email_verification(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            verification = EmailVerification.objects.get(email=email)
            verification.code = random.randint(1111, 9999)
            verification.save()
        except EmailVerification.DoesNotExist:
            verification = EmailVerification.objects.create(
                email=email,
                code=random.randint(1111, 9999)
            )
        return JsonResponse({'message': 'code sent'})

