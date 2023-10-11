from django import forms


class DoctorSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search for a Doctor')
