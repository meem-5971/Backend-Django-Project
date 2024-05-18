from django.db import models
from brand.models import Brand 
from django.contrib.auth.models import User
from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    price=models.IntegerField()
    quantity=models.IntegerField()
    buyer = models.ManyToManyField(User, blank=True) 
    car_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car/media/uploads/', blank = True, null = True)
    def __str__(self):
        return self.title 

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Comments by {self.name}"
