from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Password", validators=[validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email Address")

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def clean_email(self):
        user_email = self.cleaned_data["email"]
        users = list(User.objects.raw(f"SELECT * FROM auth_user where email='{user_email}';"))

        if users != []:
            self.add_error("email", "User with that email already exists.")

        return user_email
