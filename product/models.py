from django.db import models

# Create your models here.

class Size(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class product(models.Model):
    proid=models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=50,unique=True)

    image1=models.ImageField(upload_to="product/",blank=True,null=True)

    color=models.CharField(max_length=100)
    size=models.ManyToManyField(Size)

    price = models.IntegerField()
    def __str__(self):
        return self.name  