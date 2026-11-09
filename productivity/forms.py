from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = [
            'title',
            'description',
            'category',
            'priority',
            'deadline',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your task',
                'rows': 4
            }),

            'category': forms.Select(attrs={
                'class': 'form-control'
            }),

            'priority': forms.Select(attrs={
                'class': 'form-control'
            }),

            'deadline': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
        }