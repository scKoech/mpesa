from __future__ import unicode_literals
from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse, JsonResponse
from django_daraja.mpesa import utils
from django.views.generic import View
from decouple import config
from datetime import datetime


cl = MpesaClient()
stk_pus_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'


def oauth_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)


def index(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        amount = request.POST.get('amount')
        amount = int(amount)
        account_reference = "SANDRA"
        transaction_desc = 'STK Push Description'
        callback_url = stk_pus_callback_url
        r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return JsonResponse(r.response_description, safe=False)

    return render(request, 'index.html')
