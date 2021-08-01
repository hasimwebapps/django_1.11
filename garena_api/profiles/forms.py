from django import forms
from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Users
from .utils import generate_referral_code
from django.contrib.auth.hashers import make_password, check_password


class UsersLoginForm(ModelForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)


class UsersForm(ModelForm):
    # referral_code = forms.CharField(required=False, label=_('Referral Code'), help_text=_(
    #     'Input the referral code from another user'))
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    referral_code = forms.CharField(label='Referral Code', max_length=100, required=False)

    def __init__(self, *args, **kwargs):
        super(UsersForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Users
        fields = [
            'name',
            'username',
            'email',
            'password',
        ]

    # def save_model(self, commit=True):
    #     user = super(UsersForm, self).save(commit=False)
    #     user.username = self.cleaned_data['username']
    #
    #     hashed_pwd = make_password(self.cleaned_data['password'])
    #     print(check_password(self.cleaned_data['password'], hashed_pwd))
    #     print(hashed_pwd)
    #
    #     user.password = hashed_pwd
    #     user.name = self.cleaned_data['email']
    #     user.email = self.cleaned_data['email']
    #     user.referral = generate_referral_code()
    #
    #     if commit:
    #         user.save()
