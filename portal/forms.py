from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ["name", "email", "phone", "category", "address", "area", "description", "photo"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Describe the issue and any useful landmarks..."}),
            "address": forms.TextInput(attrs={"placeholder": "Street, landmark and locality"}),
            "area": forms.TextInput(attrs={"placeholder": "Ward / neighbourhood"}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=80, required=True)
    class Meta:
        model = User
        fields = ("username", "first_name", "email", "password1", "password2")
