from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()


class RegisterForm(forms.ModelForm):
    repeat_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'repeat_password',
            'first_name',
            'last_name',
            'email',
            'age',
            'phone_number',
            'avatar',
            'bio'
        )

    def clean(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['repeat_password']
        if not password == re_password:
            raise forms.ValidationError('Passwords must match')
        data = self.cleaned_data
        data.pop('repeat_password')
        return data

    def clean_username(self):
        username = self.cleaned_data['username']
        que = User.objects.filter(username=username)
        if que:
            raise forms.ValidationError('Username is Already taken!')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        que = User.objects.filter(email=email)
        if que:
            raise forms.ValidationError('email is Already taken!')
        return email

    def save(self, commit=True):
        password = self.cleaned_data['password']
        self.instance.password = make_password(password)
        self.instance.save()
        return self.instance


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'avatar',
        )
