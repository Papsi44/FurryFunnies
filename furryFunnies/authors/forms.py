from django import forms

from furryFunnies.authors.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "first_name", "last_name", "passcode", "pets_number"

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'personal_photo': forms.TextInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'pets_number': forms.TextInput(attrs={'placeholder': 'Enter the number of your pets...'})
        }

        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'passcode': 'Passcode:"',
            'pets_number': 'Pets Number:"',
        }
        error_messages = {
            'first_name': {
                'required': 'Please enter your first name.',
                'min_length': 'First name must be at least 4 characters long.',
            },
            'last_name': {
                'required': 'Please enter your last name.',
                'min_length': 'Last name must be at least 2 characters long.',
            },
            'passcode': {
                'required': 'Please enter a passcode.',
                'invalid': 'Passcode must be a valid number.',
            },
            'pets_number': {
                'required': 'Please enter the number of your pets.',
                'invalid': 'Please enter a valid number.',
            },
        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields['first_name'].widget.attrs['placeholder'] = "Enter your first name..."
    #     self.fields['first_name'].label = "First Name:"
    #
    #     self.fields['last_name'].widget.attrs['placeholder'] = "Enter your last name..."
    #     self.fields['last_name'].label = "Last Name:"
    #
    #     self.fields['passcode'].widget.attrs['placeholder'] = "Enter 6 digits..."
    #     self.fields['passcode'].label = "Passcode:"
    #
    #     self.fields['pets_number'].widget.attrs['placeholder'] = "Enter the number of your pets..."
    #     self.fields['pets_number'].label = "Pets Number:"

class AuthorCreateForm(AuthorBaseForm):
    pass
