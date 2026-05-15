from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class PG(models.Model):

    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    rent=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to='pg_images/')
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Review(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    pg=models.ForeignKey(PG, on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.user.username

    