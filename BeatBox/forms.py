from django import forms
from crispy_forms.helper import FormHelper
from .models import profile, post
from django.contrib.auth.forms import UserChangeForm
class profileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']
    def __init__(self, *args, **kwargs):
        super(profileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        for field in profileForm.Meta.fields:
            self.fields[field].label = False
class EditForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ["content", "image"]
class EditLikesForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ["likes"]
