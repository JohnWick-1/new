from django.contrib import admin
from .models import Student,Student2
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','marks','DOB']
    print('inside StudentAdmin')


class Student2Admin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'marks', 'DOB']
    print('inside Student2Admin')




admin.site.register(Student,StudentAdmin)
admin.site.register(Student2,Student2Admin)

