from django import forms
from .models import Profile, Neighbourhood, Business, Post


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Name'].widget = forms.TextInput()

    class Meta:
        model = Profile
        exclude = ('user', 'is_admin', 'neighbourhood')

