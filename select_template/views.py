from django.shortcuts import render
from newtracker.users.models import Student
# Create your views here.
def select_for_single(request, **kwargs):
    return render(request, 'single.html',{ 'pk':kwargs.get('pk')})

def basketball(request, **kwargs):
    student = Student.objects.get(pk=kwargs.get('pk'))
    return render(request, 'basketball.html',{ 'pk':kwargs.get('pk'), 'student':student})

def clean(request, **kwargs):
    student = Student.objects.get(pk=kwargs.get('pk'))
    return render(request, 'clean.html',{ 'pk':kwargs.get('pk'), 'student':student})

def select_multiple_students(request, **kwargs):
    return render(request, 'multi.html',{ 'pk':kwargs.get('pk')})

def business(request, **kwargs):
    students = Student.get_students_by_ids(request.session['ids'])
    return render(request, 'business.html', {'students':students})