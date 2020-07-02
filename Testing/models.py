from django.db import models

# Create your models here.
class DataTesting(models.Model):
    image = models.CharField(max_length=100, blank=True)
    label = models.CharField(max_length=50, blank=True)
    directory = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.image)