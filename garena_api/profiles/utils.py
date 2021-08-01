import os
import base64
import uuid
import hashlib


def generate_referral_code(length=8):
    token = os.urandom(length)
    return base64.b64encode(token)


def generate_err_ret():
    return {
        "base": {
            "status": 1,
            "message": "error"
        },
        "err_msg": "Internal Error"
    }


def generate_ret():
    return {
        "base": {
            "status": 0,
            "message": "success"
        },
    }

