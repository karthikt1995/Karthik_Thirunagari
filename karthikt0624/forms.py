# contactapp/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['date_created']

    def clean_contact_name(self):
        contact_name = self.cleaned_data.get('contact_name')
        if Contact.objects.filter(contact_name=contact_name).exists():
            raise ValidationError("Contact with this name already exists.")
        return contact_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Contact.objects.filter(email=email).exists():
            raise ValidationError("Contact with this email already exists.")
        return email
    
    def clean_notes(self):
        # Add any specific validation for the notes field if needed
        notes = self.cleaned_data.get('notes')
        # Your validation logic here
        return notes

