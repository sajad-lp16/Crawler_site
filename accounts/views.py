from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from . import forms

User = get_user_model()


class LoginUser(generic.View):
    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST['next'])
                return redirect('movies:home')
        return self.get(request, *args, **kwargs)


class LogOutUser(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('movies:home')


class RegisterUser(generic.CreateView):
    form_class = forms.RegisterForm
    queryset = User.objects.all()
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('movies:home')


class UserProfile(generic.DetailView):
    model = User
    template_name = 'profile_view.html'
    context_object_name = 'user'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect('movies:home')
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user


class EditProfile(generic.UpdateView):
    model = User
    template_name = 'edit_profile.html'
    fields = 'username', 'email', 'phone_number', 'avatar', 'first_name', 'last_name', 'age'
    success_url = reverse_lazy('movies:home')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect('movies:home')
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user
