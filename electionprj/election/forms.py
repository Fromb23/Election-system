from django import forms
from .models import Voter
from .models import County, Constituency, Ward, PollingStation

class VoterForm(forms.Form):
    # class Meta:
        #model = Voter
        # fields = [
        #        'first_name', 'last_name', 'email', 'password', 'national_id',
        #       'phone_number', 'date_of_birth'
        #        ]
        # widgets = {
        #        'password': forms.PasswordInput(),
        #       }
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    national_id = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)
    date_of_birth = forms.DateField()

    def save_voter(self, commit=True):
        email = self.cleaned_data['email']
        if Voter.objects.filter(email=email).exists():
            print("A similar user already exists")
        else:
            voter = Voter(
                    first_name = self.cleaned_data['first_name'],
                    last_name = self.cleaned_data['last_name'],
                    email = self.cleaned_data['email'],
                    password = self.cleaned_data['password'],
                    national_id = self.cleaned_data['national_id'],
                    phone_number = self.cleaned_data['phone_number'],
                    date_of_birth = self.cleaned_data['date_of_birth']
                    # voted = self.cleaned_data['voted']
                    )
    
            if commit:
                voter.save()
    
        return voter
    
class FilterForm(forms.Form):
    county = forms.ModelChoiceField(queryset=County.objects.all(), required=False, label="County")
    constituency = forms.ModelChoiceField(queryset=County.objects.none(), required=False, label="Constituency")
    ward = forms.ModelChoiceField(queryset=County.objects.none(), required=False, label="Ward")
    polling_station = forms.ModelChoiceField(queryset=County.objects.none(), required=False, label="Polling Station")

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        if 'County' in self.data:
            try:
                county_id =int(self.data.get('county'))
                self.fields['constituency'].queryset = Constituency.objects.filter(county_id=county_id).order_by('name')
            except (ValueError, TypeError):
                print('County not found')
        #elif self.instance.pk:
            # self.field['constituency'].queryset = self.instance.county.contituencies.order_by('name')

        if 'constituency' in self.data:
            try:
                constituency_id = int(self.data.get('constituency'))
                self.fields['ward'].queryset = Ward.objects.filter(constituency_id=constituency_id).order_by('name')
            except (ValueError, TypeError):
                print('Constituency not Found, pls check')
        # elif self.instance.pk:
            # self.fields['ward'].queryset = self.instance.constituency.ward.order_by('name')

        if 'ward' in self.data:
            try:
                ward_id = int(self.data.get('ward'))
                self.fields['polling_station'].queryset = PollingStation.objects.filter(ward_id=ward_id).order_by('name')
            except (ValueError, TypeError):
                print("Ward not found")
