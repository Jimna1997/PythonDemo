from django import forms

class RegisterForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # dob = forms.EmailField(widget=forms.DateField(attrs={'class':'form-control'}))
    age = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    gender = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    phn_no = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
