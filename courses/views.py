from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseCreateForm

def course_list(request):
    items = Course.objects.all()
    return render(request, 'courses/course_list.html', {'items': items})

def course_create(request):
    # manual form
    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            Course.objects.create(
                code=form.cleaned_data['code'],
                name=form.cleaned_data['name']
            )
            return redirect('courses:list')
    else:
        form = CourseCreateForm()
    return render(request, 'courses/course_form.html', {'form': form, 'title': 'Create Course'})

def course_update(request, pk):
    obj = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            obj.code = form.cleaned_data['code']
            obj.name = form.cleaned_data['name']
            obj.save()
            return redirect('courses:list')
    else:
        form = CourseCreateForm(initial={'code': obj.code, 'name': obj.name})
    return render(request, 'courses/course_form.html', {'form': form, 'title': 'Update Course'})

def course_delete(request, pk):
    obj = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('courses:list')
    return render(request, 'courses/course_confirm_delete.html', {'obj': obj})
