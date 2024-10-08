from django import forms
from .models import Voter
from .models import County, Constituency, Ward, PollingStation

class VoterForm(forms.Form):
    class Meta:
        model = Voter
        fields = [
                'first_name', 'last_name', 'email', 'password', 'national_id',
                'phone_number', 'date_of_birth'
                ]
        widgets = {
                'password': forms.PasswordInput(),
                }
    
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
