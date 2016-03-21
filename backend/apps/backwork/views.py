from django.shortcuts import render
from apps.backwork.models import TCustomerMstr
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
import json
# Create your views here.

@csrf_exempt
def login_user(request):
    data =''
    request_data =''
    username = 'hello'
    password = 'hello'
    credentials = ''
    print "outside"
    request_data = json.loads(request.body)
    print request_data
    if request.method == 'POST':
        username= request_data['username']
        password = request_data['password']
        print password
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        credentials = [username,password]
        data = json.dumps(credentials)
        print user
    return HttpResponse(data)
      
       
    