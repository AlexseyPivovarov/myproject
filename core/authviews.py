from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import View

from .forms import Profile


class SignUpView(View):

    def get(self, request):
        return render(request, 'auth/registration.html', {'reg_form': UserCreationForm()})

    def post(self, request):
        post_form = UserCreationForm(request.POST)
        if post_form.is_valid():
            username = post_form.cleaned_data['username']
            password = post_form.cleaned_data['password1']
            User.objects.create_user(username=username, password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')


class ProfileView(View):

    def get(self, request):
        return render(request, 'auth/profile.html', {'form': Profile(instance=request.user)})

    def post(self, request):
        form = Profile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

