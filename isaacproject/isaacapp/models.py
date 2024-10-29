from django.db import models

# Create your models here.
class ActiveItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    unlock = models.TextField()
    quality = models.SmallIntegerField()
    
    def __str__(self):
        return self.name