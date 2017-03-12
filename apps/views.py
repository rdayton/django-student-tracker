from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.users.models import User, Student
from apps.users.forms import StudentSearchForm, MultiSubmitForm


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
        if 'submit' in request.POST:
            form = StudentSearchForm(request.POST)
            if form.is_valid():
                if is_number(gpa): 
                    gpa = float(gpa)   
                students = Student.get_search_results(gpa=gpa, major=major)
        elif 'multi-submit' in request.POST:
            form = MultiSubmitForm(request.POST)
            if form.is_valid():
                request.session['ids'] = request.POST.getlist('choices')
                return redirect('select_template:multi')
            

        

    return render(request, 'pages/home.html',{
        'students': students, 'form':form, 
    })