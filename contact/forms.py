from django import forms


# Contact form from LearnDjango.com
class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50, required=True)
    email_address = forms.EmailField(max_length=150, required=True)
    subject = forms.CharField(max_length=150, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
