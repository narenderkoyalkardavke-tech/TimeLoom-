
from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'category',
        'priority',
        'deadline',
        'is_completed',
        'created_at',
    )

    list_filter = (
        'category',
        'priority',
        'is_completed',
    )

    search_fields = (
        'title',
        'description',
        'user__username',
    )

    list_editable = (
        'is_completed',
        'priority',
    )
