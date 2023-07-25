from django.db import models
import os


def get_img_upload_path(instance, filename):
    return f"car_images/{instance.car.name}/{filename}"


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
    image = models.ImageField(upload_to="car_images", null=True)

    class Meta:
        ordering = ["category", "name"]

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)

        super(Car, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name


class TechSheet(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="tech_sheets")
    heading = models.CharField(max_length=88)
    paragraph = models.TextField()
    image = models.ImageField(upload_to=get_img_upload_path)


class TechSlide(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="tech_slides")
    heading = models.CharField(max_length=40)
    paragraph = models.TextField()
    image = models.ImageField(upload_to=get_img_upload_path)
