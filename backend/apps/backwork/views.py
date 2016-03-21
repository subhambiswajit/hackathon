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
    data = ''
    username = ''
    password = ''
    if request.POST:
        try:
            username = request.POST['username']
            password = request.POST['password']
            print username
            print password
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print '>>>>>>>>>>>>.'
                print username
                print password
                credentials = [username,password]
                data = json.dumps(credentials)
                return HttpResponse(data)
            else:
                raise ObjectDoesNotExist
        except  ObjectDoesNotExist:
            credentials = [username,password]
            data = json.dumps(credentials)
            return HttpResponse(data)
       
    