from django.db import models

# Create your models here.
class Food(models.Model):
    name=models.CharField(max_length=250)
    ing=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

