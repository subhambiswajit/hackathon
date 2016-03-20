from django.shortcuts import render
from apps.backwork.models import TCustomerMstr
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@csrf_exempt
def login_user(request):
    data = ''
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            raise ObjectDoesNotExist
        print '>>>>>>>>>>>>.'
        print username
        print password
        credentials = [username,password]
        data = json.dumps(credentials)
    return HttpResponse(data)