from django.db import models

# Create your models here.

class About(models.Model):
        
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)


