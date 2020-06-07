from django import forms
from app1.models import User

class SignupForm(forms.ModelForm):
    # Form fields
    username = forms.CharField(widget=forms.TextInput(attrs={'name':'username', 'type':'text', 'id':'user_username', 'class':'form-control', 'required':True, 'placeholder':"Enter Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'name':'user_password', 'type':'password', 'id':'InputPassword', 'class':'form-control', 'required':True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'name':'user_email', 'type':'email', 'id':'InputEmail', 'class':'form-control', 'required':True}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'name':'first_name', 'type':'text', 'id':'user_first_name', 'class':'form-control', 'required':True}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'name':'last_name', 'type':'text', 'id':'user_last_name', 'class':'form-control', 'required':True}))
    delivery_address = forms.CharField(widget=forms.TextInput(attrs={'name':'delivery_address', 'type':'text', 'id':'user_address', 'class':'form-control', 'required':True}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'name':'phone_number', 'type':'number', 'id':'user_phone_number', 'class':'form-control', 'required':True}))
    class Meta:
        model = User
        fields = "__all__"
    