from django import forms
from .models import Student
from courses.models import Course

class StudentForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Courses"
    )

    class Meta:
        model = Student
        fields = ['name', 'age', 'image', 'date_of_birth', 'courses']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if getattr(self.instance, 'pk', None):
            self.fields['courses'].initial = self.instance.courses.all()
