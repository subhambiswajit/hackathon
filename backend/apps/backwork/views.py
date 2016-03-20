from django.shortcuts import render
from apps.backwork.models import TCustomerMstr
from django.http import HttpResponse
# Create your views here.


def login_user(request):
    if request.POST:
        try:
            username = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            print user
            if user is not None:
                login(request, user)
                return HttpResponse('The user is loggen in succesfully')
            else:
                raise ObjectDoesNotExist
        except  ObjectDoesNotExist:
            messages.warning(request,"Wrong username or password")
            return HttpResponse('User not logged in')