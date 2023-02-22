from django.contrib import admin
from .models import Department,Student

# Register your models here.
class deptAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Department,deptAdmin)

admin.site.register(Student)