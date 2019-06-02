from django.db import models
from django.utils import timezone

class Animals(models.Model):
    animal= models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    def __str__(self):
        return self.animal
class Post(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    favourite_color = models.CharField(max_length=200)
    favourite_animal = models.ForeignKey(Animals, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)
    def __str__(self):
        return self.name_text
