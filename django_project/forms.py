from django import forms

class usersForm(forms.Form):
    num1 = forms.CharField(label="Value 1", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    num2 = forms.CharField(label="Value 2", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email")

class evenOdd(forms.Form):
    num = forms.CharField(label="Number", required=False)