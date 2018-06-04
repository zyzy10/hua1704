from django import forms
# from django.forms import ValidationError

from .models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nlck','pssword','icon','sex','age']
    password2 = forms.CharField(required=True,max_length=200)


    def clean_pssword2(self):
        cleaned_data = super().clean()
        if len(cleaned_data['pssword']) <= 8:
            raise forms.ValidationError('密码长度过短')
        elif cleaned_data['pssword'] != cleaned_data['password2']:
            raise forms.ValidationError('密码不一致')
