from django.db import models


class Products(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    url = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.title


