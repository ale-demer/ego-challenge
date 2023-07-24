from django.db import models
import os

CATEGORY_CHOICES = (
    ("1", "Autos"),
    ("2", "Pickups y Comerciales"),
    ("3", "SUVs y Crossovers"),
)


class Car(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="1")
    title = models.CharField(max_length=50)
    description = models.TextField()
    year = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="car_images", blank=True, null=True)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)

        super(Car, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name
