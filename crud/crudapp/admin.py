from django.contrib import admin
from crudapp.models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['Name','Age','Dep','cgpa','project','clubs']
admin.site.register(Student,StudentAdmin)
