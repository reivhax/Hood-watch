from django import forms
from .models import Profile, Neighbourhood, Business, Post


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Name'].widget = forms.TextInput()

    class Meta:
        model = Profile
        exclude = ('user', 'is_admin', 'neighbourhood')


class HoodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Name'].widget = forms.TextInput()
        self.fields['police'].widget = forms.TextInput()
        self.fields['health'].widget = forms.TextInput()

    class Meta:
        model = Neighbourhood
        exclude = ('admin',)


class BizForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Name'].widget = forms.TextInput()

    class Meta:
        model = Business
        exclude = ('owner','neighbourhood')


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Text'].widget = forms.TextInput()

    class Meta:
        model = Post
        exclude = ('user', 'neighbourhood')
