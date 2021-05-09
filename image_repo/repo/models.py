from django.db import models

# Create your models here.


class Tags(models.Model):
    tag = models.CharField(max_length=20)

class User(models.Model):
    name = models.CharField(max_length=50)

class Item(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.URLField(max_length=400)
    num_reviews = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10.99)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventory', default=1, blank=True, null=True)

    def __str__(self):
        return f'{self.id}: {self.name} | ${self.price} | {self.image_url}'
#
