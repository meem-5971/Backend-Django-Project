from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=15)
    description=models.TextField()
    completion=models.BooleanField(default=False)
    category=models.ManyToManyField(Category)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title