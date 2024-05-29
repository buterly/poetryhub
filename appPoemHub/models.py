from django.db import models

# Create your models here.

class Poems(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    poem = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

    