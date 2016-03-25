from django.shortcuts import render
from apps.backwork.models import GlobalUsers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage

import json
import datetime 
import random
# Create your views here.

@csrf_exempt
def signup_user(request):
    request_data = json.loads(request.body)
    # request_data = request.GET
    back = ''
    data = False
    hasher =''
    verify_code = ''
    username_check = GlobalUsers.objects.filter(gus_email= request_data['email']).values_list('gus_email', flat=True)
    if request.method == 'POST' and request_data['email'] not in username_check:
        data = True
        verify_code = str(random.randint(10000,99999))
        hasher = PBKDF2PasswordHasher()
        signup_details = GlobalUsers()
        # signup_details.gus_username = str(request_data['username'])
        signup_details.gus_password = hasher.encode(password= request_data['password'] , salt='salt',iterations= 50000)
        signup_details.gus_email = request_data['email']
        signup_details.gus_address = request_data['address']
        signup_details.gus_pincode = request_data['pincode']
        signup_details.gus_createdon = datetime.datetime.now()
        signup_details.gus_isused = 0
        signup_details.gus_confirmcode = verify_code
        signup_details.gus_phone = request_data['phone']
        signup_details.save()
        subject = "email verification HUL"            
        message = "please verify your email by typing the following code in your Distributor App " + verify_code
        sender = "hul@gmail.com"
        send_mail(subject, message, sender, [request_data['email']])
        back = [{'hello':'hello'}]
        data = json.dumps(back)
        print request_data
    return HttpResponse(data)

@csrf_exempt
def user_login(request):
	# request_data = json.loads(request.body)
    request_data = json.loads(request.body)
    username = ''
    password = ''
    data = ''
    username = request_data['username']
    print username
    password = request_data['password']
    print password
    if request.method == 'POST':
    	try:
    		user = authenticate(username=username, password=password)
    		if user is not None:
    		    data = True
    		    login(request, user)
    		    return HttpResponse(data)
    		else:
    		    raise ObjectDoesNotExist
    	except  ObjectDoesNotExist:
    	    data = False
    	    return HttpResponse(data)

      
       
    