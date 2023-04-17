from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import FormView

# Create your views here.
    
class RegisterPage(FormView):
    form_class = UserCreationForm
    redirect_authenticated_user  = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login (self.request, user)
        return super(RegisterPage, self).form_valid(form)
    def get(self, *args, **kwargs) :
        if self.request.user.is_authenticated:
            return redirect ('index')
        return super(RegisterPage, self).get(*args,  **kwargs)  
