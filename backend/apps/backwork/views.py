from django.shortcuts import render
from apps.backwork.models import GlobalUsers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
import json
import datetime 
import random
# Create your views here.

@csrf_exempt
def signup_user(request):
    request_data = json.loads(request.body)
    back = ''
    data =''
    print request_data
    if request.method == 'POST':
        hasher = PBKDF2PasswordHasher()
        signup_details = GlobalUsers()
        signup_details.gus_username = request_data['username']
        signup_details.gus_password = hasher.encode(password= request_data['password'] , salt='salt',iterations= 50000)
        signup_details.gus_email = request_data['email']
        signup_details.gus_address = request_data['address']
        signup_details.gus_pincode = request_data['pincode']
        signup_details.gus_createdon = datetime.datetime.now()
        signup_details.gus_isused = 0
        signup_details.gus_confirmcode = str(random.randint(10000,99999))
        signup_details.gus_phone = request_data['phone']
        signup_details.save()
        back = {'hello':'hello'}
        data = json.dumps(back)
    return HttpResponse(data)

      
       
    