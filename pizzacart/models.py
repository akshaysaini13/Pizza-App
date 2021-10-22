from django.db import models

# Create your models here.

class Product(models.Model):
    eid = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    mrp = models.IntegerField(default=0)
    image = models.ImageField(upload_to="pizzacart/images", default="")
    date = models.DateField()

    def __str__(self):
        return str(self.eid) + " " + self.title