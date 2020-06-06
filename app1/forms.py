from django import forms
from app1.models import User

class SignupForm(forms.ModelForm):
    # Form fields
    class Meta:
        model = User
        fields = "__all__"
