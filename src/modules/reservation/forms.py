from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class SignupForm(forms.Form):
    """Signup form."""
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True)

    def clean(self):
        """Validate password1 eq password2"""
        form_data = super(SignupForm, self).clean()

        if form_data["password1"] != form_data["password2"]:
            del form_data['password1']
            del form_data['password2']
            forms.ValidationError("Passwords do not match")

        try:
            User.objects.get(email=form_data["email"])
            del form_data["email"]
            forms.ValidationError("Email already registered")
        except ObjectDoesNotExist:
            # email is unique
            pass

        return form_data


class LoginForm(forms.Form):
    """Login form."""
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    def clean(self):
        """Check if user exists and valid email and password."""
        form_data = super(LoginForm, self).clean()

        user = None
        try:
            user = User.objects.get(email=form_data["email"])
        except ObjectDoesNotExist:
            forms.ValidationError("Invalid email or password")

        if user:
            user = authenticate(username=user.username, password=form_data["password"])
            if not user:
                forms.ValidationError("Invalid email or password")
            else:
                form_data["user"] = user
        return form_data
