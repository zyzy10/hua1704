from django import forms

from .models import Comments


class ModelsForm(forms.Form):
    class Meta:
        model = Comments
        fields = ['title','content']



