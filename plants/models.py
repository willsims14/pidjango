import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Plant(models.Model):
    common_name = models.CharField(max_length=200, unique=True)
    scientific_name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='plants/images')
    slug = models.SlugField(max_length=200, unique=True)
    meta_created = models.DateTimeField(auto_now_add=True)
    meta_modified = models.DateTimeField(auto_now=True)

    # def number_of_propogations(self):
    #     return len(self.propogations)

    # def __str__(self):
    #     return f"<Plant> {self.common_name}"


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

    def __str__(self):
        return f"<Plant.Propogation> {self.plant.common_name} (Location: {self.prop_location})"

    def was_propogated_recently(self):
        return self.date_propped >= timezone.now() - datetime.timedelta(days=1)
