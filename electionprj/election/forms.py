from django import forms
from .models import Voter

class VoterForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = [
                'first_name', 'last_name', 'email', 'password', 'national_id',
                'phone_number', 'date_of_birth'
                ]
        widgets = {
                'password': forms.PasswordInput(),
                }
