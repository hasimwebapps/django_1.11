import json
from django.shortcuts import render
from profiles.models import Users
from django.http import JsonResponse


# Create your views here.

def show(request):
    db_results = list(Users.objects.all())
    # users = []
    # for e in db_results:
    #     print(e)
    return JsonResponse({'ping': db_results})
