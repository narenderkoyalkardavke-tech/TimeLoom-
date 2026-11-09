from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    CATEGORY_CHOICES = [
        ('Study', 'Study'),
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Project', 'Project'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Personal'
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )

    deadline = models.DateTimeField(
        null=True,
        blank=True
    )

    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
