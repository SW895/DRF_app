from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=250, unique=True)
    email = models.EmailField()

    class Meta:
        ordering = ('name')

    def __str__(self):
        return self.name