from django.db import models

class Message(models.Model):
    PROJECT_CHOICES = [
        ('web_development', 'Web Development'),
        ('api_development', 'API Development'),
        ('database_design', 'Database Design'),
        ('consultation', 'Consultation'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField()
    project_type = models.CharField(max_length=50, choices=PROJECT_CHOICES)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
