from django.contrib import admin
from basic_app.models import Student, School

class Student_Detial(admin.ModelAdmin):
    list_display = ('name', 'school')


admin.site.register(School)
admin.site.register(Student,Student_Detial)
