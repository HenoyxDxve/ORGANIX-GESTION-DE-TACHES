from django.contrib import admin

# Register your models here.
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'priority', 'status', 'created_at')
    list_filter = ('priority', 'status', 'due_date')
    search_fields = ('title', 'description')
    ordering = ('due_date',)