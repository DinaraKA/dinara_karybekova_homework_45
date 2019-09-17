from django.contrib import admin
from webapp.models import Task

class TaskAdmin(admin.ModelAdmin):

    list_display = ['id', 'description', 'status', 'date']
    list_filter = ['status']
    search_fields = ['description']
    fields = ['description', 'status', 'details', 'date']


admin.site.register(Task, TaskAdmin)