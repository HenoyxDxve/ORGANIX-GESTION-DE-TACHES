from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Faible'),
        ('medium', 'Moyenne'),
        ('high', 'Haute'),
    ]

    STATUS_CHOICES = [
        ('todo', 'À faire'),
        ('in_progress', 'En cours'),
        ('done', 'Terminée'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # tri : la priorité haute (high) passe avant (car alphabetiquement h < m < l)
        ordering = ['status', 'due_date', 'priority']

    def __str__(self):
        return self.title
