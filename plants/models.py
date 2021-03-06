import datetime

from django.shortcuts import reverse
from django.utils import timezone
from django.db import models


# Create your models here.
class Plant(models.Model):
    common_name = models.CharField(max_length=200, unique=True)
    scientific_name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/plants', blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    meta_created = models.DateTimeField(auto_now_add=True)
    meta_modified = models.DateTimeField(auto_now=True)

    # def number_of_propogations(self):
    #     return len(self.propogations)

    def __str__(self):
        return f"{self.common_name}"

    def get_absolute_url(self):
        return reverse(
            "plants:detail", kwargs={
            "pk": self.pk
        })


# class Plant_In_Home(Plant):
#     # plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     planted_location = models.CharField(max_length=200)
#     date_planted = models.DateField()

#     def __str__(self):
#         return f"<Plant.PlantInHome> {self.plant.common_name} (Location: {self.planted_location})"


class Propogation(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    prop_location = models.CharField(max_length=200)
    date_propped = models.DateField()
    meta_created = models.DateTimeField(auto_now_add=True)
    meta_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.plant.common_name} (Location: {self.prop_location})"

    # @classmethod
    # def create(cls, title):
    #     book = cls(title=title)
    #     book.meta_created = timezone.now()
    #     return book

    def was_propogated_recently(self):
        return self.date_propped >= timezone.now() - datetime.timedelta(days=1)
