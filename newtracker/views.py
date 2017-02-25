from django.shortcuts import render, redirect
from django.http import HttpResponse
from newtracker.users.models import User, Student
from newtracker.users.forms import StudentSearchForm
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
    gpa = request.POST.get('gpa','')
    major = request.POST.get('major','')
    form = StudentSearchForm()
    
    if request.method == 'POST':
        form = StudentSearchForm(request.POST)
        if form.is_valid():
            if is_number(gpa): 
                gpa = float(gpa)   
            students = Student.get_search_results(gpa=gpa, major=major)
        

    return render(request, 'pages/home.html',{
        'students': students, 'form':form,
    })