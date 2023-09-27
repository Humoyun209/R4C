from django import forms


class CustomerForm(forms.Form):
    email = forms.EmailField(max_length=255)
