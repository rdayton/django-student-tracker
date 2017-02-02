from django.shortcuts import render, redirect
from django.http import HttpResponse
from newtracker.users.models import User

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        new_name_input = request.POST['name_input']
        User.objects.create_user(new_name_input)
        return redirect('/')


    return render(request, 'pages\home.html',{
        'new_name_input': request.POST.get('name_input',''),
    })