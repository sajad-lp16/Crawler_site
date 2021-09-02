from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from . import forms

User = get_user_model()


class RegisterUser(generic.CreateView):
    form_class = forms.RegisterForm
    queryset = User.objects.all()
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


# class ProfileEdit(LoginRequiredMixin, generic.UpdateView):
#     queryset = User.objects.all()
#     form_class = forms.ProfileForm
#     template_name = 'edit_profile.html'
#     success_url = reverse_lazy('home')
#
#     def get_object(self, queryset=None):
#         return self.request.user
