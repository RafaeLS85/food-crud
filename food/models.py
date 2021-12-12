from django.db import models

# Create your models here.
class Food(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.CharField(max_length=500, default="https://toppng.com/uploads/preview/clipart-free-seaweed-clipart-draw-food-placeholder-11562968708qhzooxrjly.png")
