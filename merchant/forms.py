from django import forms
from products.models import Phone

class SignupForm(forms.ModelForm):
    # Form fields
    username = forms.CharField(validators=[username_validator], widget=forms.TextInput(attrs={'name':'username', 'type':'text', 'id':'user_username', 'class':'form-control', 'required':True, 'placeholder':"Enter Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'name':'user_password', 'type':'password', 'id':'InputPassword', 'class':'form-control', 'required':True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'name':'user_email', 'type':'email', 'id':'InputEmail', 'class':'form-control', 'required':True, 'placeholder':"Enter Email"}))
    first_name = forms.CharField(validators=[flname_validator], widget=forms.TextInput(attrs={'name':'first_name', 'type':'text', 'id':'user_first_name', 'class':'form-control', 'required':True, 'placeholder':"Enter First Name"}))
    last_name = forms.CharField(validators=[flname_validator], widget=forms.TextInput(attrs={'name':'last_name', 'type':'text', 'id':'user_last_name', 'class':'form-control', 'required':True, 'placeholder':"Enter Last Name"}))
    delivery_address = forms.CharField(validators=[address_validator], widget=forms.TextInput(attrs={'name':'delivery_address', 'type':'text', 'id':'user_address', 'class':'form-control', 'required':True, 'placeholder':"Enter Delivery Address"}))
    phone_number = forms.CharField(validators=[phonenum_validator], widget=forms.NumberInput(attrs={'name':'phone_number', 'type':'number', 'id':'user_phone_number', 'class':'form-control', 'required':True, 'placeholder':"Enter Phone Number"}))

    product_name = forms.CharField(widget=forms.TextInput(attrs={'name':'product_name', 'type':'text', 'id':'product_name', 'class':'form-control', 'required':True, 'placeholder':"Enter Product Name"})))
    color = forms.CharField(widget=forms.TextInput(attrs={'name':'color', 'type':'text', 'id':'color', 'class':'form-control', 'required':True, 'placeholder':"Enter Color"})))
    display = forms.CharField(widget=forms.TextInput(attrs={'name':'display', 'type':'text', 'id':'display', 'class':'form-control', 'required':True, 'placeholder':"Enter Display"}))
    storage = forms.CharField(widget=forms.TextInput(attrs={'name':'storage', 'type':'text', 'id':'storage', 'class':'form-control', 'required':True, 'placeholder':"Enter Storage"}))
    camera = forms.CharField(widget=forms.TextInput(attrs={'name':'camera', 'type':'text', 'id':'camera', 'class':'form-control', 'required':True, 'placeholder':"Enter Camera"})))
    brand = forms.CharField(widget=forms.TextInput(attrs={'name':'brand', 'type':'text', 'id':'brand', 'class':'form-control', 'required':True, 'placeholder':"Enter Brand"}))))
    processor = forms.CharField(widget=forms.TextInput(attrs={'name':'processor', 'type':'text', 'id':'processor', 'class':'form-control', 'required':True, 'placeholder':"Enter Processor"}))))
    ram = forms.CharField(widget=forms.TextInput(attrs={'name':'ram', 'type':'text', 'id':'ram', 'class':'form-control', 'required':True, 'placeholder':"Enter RAM"}))))
    price = forms.CharField(widget=forms.NumberInput(attrs={'name':'price', 'type':'number', 'id':'price', 'class':'form-control', 'required':True, 'placeholder':"Enter Price"}))))
    
    class Meta():
        model = Phone
        fields = "__all__"