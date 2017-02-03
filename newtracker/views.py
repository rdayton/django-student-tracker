from django.shortcuts import render, redirect
from django.http import HttpResponse
from newtracker.users.models import User, Student

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# Create your views here.
def home_page(request):
    gpa = None
    students = None
    gpa = request.POST.get('gpa_input','')
    if is_number(gpa):      
        gpa = float(request.POST.get('gpa_input',''))
        #user = User.objects.filter(username = name).first()       
        students = Student.objects.filter(gpa__gte = gpa)
    #user.source,created = User.objects.get_or_create( username = request.POST.get('name_input',''))
    
    return render(request, 'pages/home.html',{
        'students': students, 'gpa':gpa,
    })