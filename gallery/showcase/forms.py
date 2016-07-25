from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25)
    fname = forms.CharField(label='First Name', max_length=20)
    lname = forms.CharField(label='Last Name', max_length=20)
    email = forms.EmailField(label='Email', max_length=35)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=40)
    password_verify = forms.CharField(label='Verify Password', widget=forms.PasswordInput, max_length=40)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=40)
