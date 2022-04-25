from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main_adm/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main_adm/login.html'

    # def get_context_data(self,*,object_list=None ,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title='Авторизация')
    #     return dict(list(context.items()) + list(c_def.items()))

    # def get_success_url(self):
    #     return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')