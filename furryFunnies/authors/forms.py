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


class AuthorCreateForm(AuthorBaseForm):
    pass


class AuthorEditForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "first_name", "last_name", "pets_number", 'info', 'image_url'
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'pets_number': 'Pets Number:',
            'info': 'info:',
            'image_url': 'Profile Image URL:'
        }
        error_messages = {
            'first_name': {
                'required': 'Please enter your first name.',
                'min_length': 'First name must be at least 4 characters long.',
            },
            'last_name': {
                'required': 'Please enter your last name.',
                'min_length': 'Last name must be at least 2 characters long.',
            }
        }
class AuthorDeleteForm(AuthorBaseForm):
    pass

class AuthorDetailsForm(AuthorBaseForm):
    pass