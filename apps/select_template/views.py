from django.shortcuts import render
from apps.users.models import Student
from apps.select_template.forms import StoryForm
from django.shortcuts import get_object_or_404

# Create your views here.
def select_for_single(request, **kwargs):
    return render(request, 'single.html',{ 'pk':kwargs.get('pk')})

def basketball(request, **kwargs):
    student = get_object_or_404(Student,pk=kwargs.get('pk'))
    form = StoryForm(instance=student)
    if request.method == "POST":        
        form=StoryForm(request.POST, instance=student)
        if form.is_valid():            
            form.save()
    return render(request, 'basketball.html',{ 'pk':kwargs.get('pk'), 'student':student, 'form':form})

def clean(request, **kwargs):
    student = Student.objects.get(pk=kwargs.get('pk'))
    return render(request, 'clean.html',{ 'pk':kwargs.get('pk'), 'student':student})

def plain(request, **kwargs):
    student = Student.objects.get(pk=kwargs.get('pk'))
    return render(request, 'plain.html',{ 'pk':kwargs.get('pk'), 'student':student})

def select_multiple_students(request, **kwargs):
    return render(request, 'multi.html',{ 'pk':kwargs.get('pk')})

def business(request, **kwargs):
    students = Student.get_students_by_ids(request.session['ids'])
    return render(request, 'business.html', {'students':students})