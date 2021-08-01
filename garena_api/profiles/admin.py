from django.contrib import admin

# Register your models here.

from .models import Users
from .forms import UsersForm


class UserModelAdmin(admin.ModelAdmin):
    form = UsersForm
    list_display = ['name', 'username', 'referral', 'email']
    search_fields = ['name', 'email', 'referral']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['referral', ]
        else:
            return []


admin.site.register(Users, UserModelAdmin)
