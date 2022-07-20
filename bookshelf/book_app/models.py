from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length = 255, blank = False)

    def __str__(self):
        return self.name

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 255, blank = False)
    author = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE, default = 1)

    def __str__(self):
        return self.title