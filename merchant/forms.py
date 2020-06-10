from django import forms
from products.models import Phone

class ProductForm(forms.ModelForm):
    # Form fields
    product_name = forms.CharField(widget=forms.TextInput(attrs={'name':'product_name', 'type':'text', 'id':'product_name', 'class':'form-control', 'required':True, 'placeholder':"Enter Product Name"}))
    color = forms.CharField(widget=forms.TextInput(attrs={'name':'color', 'type':'text', 'id':'color', 'class':'form-control', 'required':True, 'placeholder':"Enter Color"}))
    display = forms.CharField(widget=forms.TextInput(attrs={'name':'display', 'type':'text', 'id':'display', 'class':'form-control', 'required':True, 'placeholder':"Enter Display"}))
    storage = forms.CharField(widget=forms.TextInput(attrs={'name':'storage', 'type':'text', 'id':'storage', 'class':'form-control', 'required':True, 'placeholder':"Enter Storage"}))
    camera = forms.CharField(widget=forms.TextInput(attrs={'name':'camera', 'type':'text', 'id':'camera', 'class':'form-control', 'required':True, 'placeholder':"Enter Camera"}))
    brand = forms.CharField(widget=forms.TextInput(attrs={'name':'brand', 'type':'text', 'id':'brand', 'class':'form-control', 'required':True, 'placeholder':"Enter Brand"}))
    processor = forms.CharField(widget=forms.TextInput(attrs={'name':'processor', 'type':'text', 'id':'processor', 'class':'form-control', 'required':True, 'placeholder':"Enter Processor"}))
    ram = forms.CharField(widget=forms.TextInput(attrs={'name':'ram', 'type':'text', 'id':'ram', 'class':'form-control', 'required':True, 'placeholder':"Enter RAM"}))
    price = forms.CharField(widget=forms.NumberInput(attrs={'name':'price', 'type':'number', 'id':'price', 'class':'form-control', 'required':True, 'placeholder':"Enter Price"}))
    
    class Meta():
        model = Phone
        fields = "__all__"