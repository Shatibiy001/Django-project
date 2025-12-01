# members/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname']  # choose your fields
        
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'John'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Doe'}),
        }
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
        }
        
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]