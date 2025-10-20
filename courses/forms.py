from django import forms

class CourseCreateForm(forms.Form):
    code = forms.CharField(max_length=10, label="Code")
    name = forms.CharField(max_length=100, label="Name")
