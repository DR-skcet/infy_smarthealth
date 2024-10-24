from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from firebase_admin import auth
from django.http import HttpResponse
import firebase_config
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            api_key = 'AIzaSyAX9CLiAa1kqUJXvqWTcENJ2JAz0NwlPBM'  # Replace with your Firebase API key
            url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"
            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": True
            }
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses

            data = response.json()
            id_token = data['idToken']  # Get ID token from the response
            
            # Here, you might want to create a session or store the ID token as needed
            messages.success(request, "Login successful!")
            return redirect('home')
        except requests.exceptions.HTTPError as e:
            error_message = e.response.json().get('error', {}).get('message', 'Unknown error')
            messages.error(request, f"Login failed: {error_message}")
    
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        try:
            # Create user in Firebase
            user = auth.create_user(
                email=email,
                password=password,
                display_name=username,
            )
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error creating user: {str(e)}")
            return render(request, 'signup.html')

    return render(request, 'signup.html')

def home(request):
    username = request.user.username
    return render(request, 'home.html', {'username': username})

import requests
from django.shortcuts import render
from django.conf import settings

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        api_key = 'AIzaSyAX9CLiAa1kqUJXvqWTcENJ2JAz0NwlPBM'  # Replace with your Firebase API Key

        url = f'https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={api_key}'
        data = {
            'requestType': 'PASSWORD_RESET',
            'email': email
        }
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Raise an error if status is not 200
            return render(request, 'password_reset_email_sent.html')
        except requests.exceptions.RequestException as e:
            error_message = e.response.json().get('error', {}).get('message', 'Unknown error occurred')
            return render(request, 'forgot_password.html', {'error': error_message})
    return render(request, 'forgot_password.html')
