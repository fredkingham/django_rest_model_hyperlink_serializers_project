from rest_framework.tests.models import RESTFrameworkModel


from django.db import models

class Meal(models.Model):
    meal_name = models.CharField(max_length=250)


class Vegetable(models.Model):
    ''' test run for a 1 -> many relationship '''
    meal = models.ForeignKey(Meal)
    vegetable_name = models.CharField(max_length=250)


class Meat(models.Model):
    ''' test run for a 1 -> 1 relationship '''
    meal = models.OneToOneField(Meal)
    meat_name = models.CharField(max_length=250)
