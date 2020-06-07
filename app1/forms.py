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
    def clean(self):
        clean_data = super().clean()
        username = clean_data['username']
        password = clean_data['password']
        email = clean_data['email']
        first_name = clean_data['first_name']
        last_name = clean_data['last_name']
        delivery_address = clean_data['delivery_address']
        phone_number = clean_data['phone_number']

        #Check if username already exists in the database
        if not(username.isalnum()):
            raise forms.ValidationError("Username is not valid. Must contain only alphanumeric characters.")
        if len(username)<4:
            raise forms.ValidationError("Username is not valid. Must contain atleast 4 characters.")
        if len(password)<10:
            raise forms.ValidationError("Password too weak.")
        if len(phone_number)!=10:
            raise forms.ValidationError("Phone number is not valid. Must contain exactly 10 digits.")
        if len(delivery_address)<20:
            raise forms.ValidationError("Please enter a valid delivery_address.")
        if not(first_name.isalpha()):
            raise forms.ValidationError("First Name should only contain alphabets. Are you Elon Musk's son? If you are, you are too young. Bye bye!")
        if not(last_name.isalpha()):
            raise forms.ValidationError("First Name should only contain alphabets.")
        
    class Meta:
        model = User
        fields = "__all__"
    
