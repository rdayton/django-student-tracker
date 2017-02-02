from django.shortcuts import render, redirect
from django.http import HttpResponse
from newtracker.users.models import User

# Create your views here.
def home_page(request):
    user = User()
    name = request.POST.get('name_input','')
    users = User.objects.filter(username=name)
    #user.source,created = User.objects.get_or_create( username = request.POST.get('name_input',''))
    

    allusers = User.objects.all()

    return render(request, 'pages/home.html',{
        'users': users,
    })