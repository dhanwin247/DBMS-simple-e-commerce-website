from django import forms
from app1.models import User


def username_validator(value):
    if not(value.isalnum()):
        raise forms.ValidationError("Username is not valid. Must contain only alphanumeric characters.")
    if len(value)<4:
        raise forms.ValidationError("Username is not valid. Must contain atleast 4 characters.")

def phonenum_validator(value):
    if len(value)!=10:
        raise forms.ValidationError("Phone number is not valid. Must contain exactly 10 digits.")

def address_validator(value):
    if len(value)<20:
        raise forms.ValidationError("Please enter a valid delivery_address.")

def flname_validator(value):
    if not(value.isalpha()):
        raise forms.ValidationError("Should only contain alphabets. Are you Elon Musk's son? If you are, you are too young. Bye bye!")


class SignupForm(forms.ModelForm):
    # Form fields
    username = forms.CharField(validators=[username_validator], widget=forms.TextInput(attrs={'name':'username', 'type':'text', 'id':'user_username', 'class':'form-control', 'required':True, 'placeholder':"Enter Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'name':'user_password', 'type':'password', 'id':'InputPassword', 'class':'form-control', 'required':True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'name':'user_email', 'type':'email', 'id':'InputEmail', 'class':'form-control', 'required':True, 'placeholder':"Enter Email"}))
    first_name = forms.CharField(validators=[flname_validator], widget=forms.TextInput(attrs={'name':'first_name', 'type':'text', 'id':'user_first_name', 'class':'form-control', 'required':True, 'placeholder':"Enter First Name"}))
    last_name = forms.CharField(validators=[flname_validator], widget=forms.TextInput(attrs={'name':'last_name', 'type':'text', 'id':'user_last_name', 'class':'form-control', 'required':True, 'placeholder':"Enter Last Name"}))
    delivery_address = forms.CharField(validators=[address_validator], widget=forms.TextInput(attrs={'name':'delivery_address', 'type':'text', 'id':'user_address', 'class':'form-control', 'required':True, 'placeholder':"Enter Delivery Address"}))
    phone_number = forms.CharField(validators=[phonenum_validator], widget=forms.NumberInput(attrs={'name':'phone_number', 'type':'number', 'id':'user_phone_number', 'class':'form-control', 'required':True, 'placeholder':"Enter Phone Number"}))

    class Meta():
        model = User
        exclude = ["userid"]
