from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=223)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)