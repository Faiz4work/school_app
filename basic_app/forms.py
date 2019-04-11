from django import forms
from .models import School,Student

class AddStudentForm(forms.ModelForm):

    class Meta():
        model = Student
        fields = ('name','age','school')
