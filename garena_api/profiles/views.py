import json
import logging
import hashlib
import base64
import uuid

from django.shortcuts import render
from profiles.models import Users
from django.http import JsonResponse
from .forms import UsersForm, UsersLoginForm
from django.views.decorators.csrf import csrf_exempt
from .utils import generate_ret, generate_err_ret
from django.contrib.auth.hashers import make_password, check_password


def user_list(request):
    ret = generate_ret()
    try:
        ret['items'] = list(Users.objects.values())
    except Exception as e:
        logging.error(e, exc_info=True)
        return JsonResponse(generate_err_ret(), status=500)

    return JsonResponse(ret)


@csrf_exempt
def user_login(request):
    ret = generate_ret()
    try:
        # ret['items'] = list(Users.objects.filter(username=))
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = list(Users.objects.filter(username=username).values())
        if len(user) > 0:
            is_valid_password = check_password(password, user[0]["password"])
            if not is_valid_password:
                ret = generate_err_ret()
                ret["err_msg"] = "Invalid Password"
                return JsonResponse(ret)

        else:
            ret = generate_err_ret()
            ret["err_msg"] = "invalid Username"
            return JsonResponse(ret)

        ret['items'] = user
    except Exception as e:
        logging.error(e, exc_info=True)
        return JsonResponse(generate_err_ret(), status=500)

    return JsonResponse(ret)


@csrf_exempt
def user_add(request):
    ret = generate_ret()
    try:
        if request.method == 'POST':
            form = UsersForm(request.POST)
            if form.is_valid():
                referral_code = form.cleaned_data['referral_code']
                if referral_code:
                    referral_code_exist = (Users.objects.filter(referral=referral_code))
                    if len(referral_code_exist) < 1:
                        ret = generate_err_ret()
                        ret["err_msg"] = 'Please Check Referral Code!'
                        return JsonResponse(ret, status=401)

                ret["items"] = form.cleaned_data
                form.save()
            else:
                ret = generate_err_ret()
                ret["err_msg"] = form.errors
                return JsonResponse(ret, status=401)
    except Exception as e:
        logging.error(e, exc_info=True)
        return JsonResponse(generate_err_ret(), status=500)

    return JsonResponse(ret)
