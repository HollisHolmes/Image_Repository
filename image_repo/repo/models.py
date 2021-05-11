from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __str(self):
        return f'{self.id}: {self.tag}'


class Item(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.URLField(max_length=400)
    num_reviews = models.IntegerField(default=0)
    price = models.FloatField(default=10.99)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventory', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='items')

    def __str__(self):
        return f'{self.id}: {self.name} | ${self.price} | {self.image_url}'

    def is_valid_item(self):
        pass


