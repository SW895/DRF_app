from django.db import models

class Mod_Category(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ('name')
    
    def __str__(self):
        return self.name