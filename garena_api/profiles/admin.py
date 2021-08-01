from django.contrib import admin

# Register your models here.

from .models import Users
from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _


class UsersForm(ModelForm):
    # referral_code = forms.CharField(required=False, label=_('Referral Code'), help_text=_(
    #     'Input the referral code from another user'))

    def __init__(self, *args, **kwargs):
        super(UsersForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Users
        fields = [
            'name',
            'username',
            'email',
        ]


class UserModelAdmin(admin.ModelAdmin):
    form = UsersForm

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['referral', ]
        else:
            return []


admin.site.register(Users, UserModelAdmin)
