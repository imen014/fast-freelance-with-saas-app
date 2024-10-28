from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model


class UserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'image', 'date_naissance','lieu_residence','social_media','description','current_employment','academic_degrees','professional_skills','hobbies']


class AuthenticatorForm(forms.Form):
    username=forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    