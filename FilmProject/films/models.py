from django.db import models


class Country(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Director(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Film(models.Model):

    title = models.CharField(max_length=150)
    release_date = models.DateTimeField(auto_now_add=True)
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')
    available_in_countries = models.ManyToManyField(Country)
    category = models.ManyToManyField(Category, related_name='category')
    director = models.ManyToManyField(Director)

    def __str__(self):
        return self.title
