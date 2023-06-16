from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import BaseUserCreationForm, UserCreationForm
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


class SignUp(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'




