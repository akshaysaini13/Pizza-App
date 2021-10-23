from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
)


TYPE_CHOICES = (
('Non-Veg', 'NON-VEG'),
('Veg', 'VEG')
)

SHAPE_CHOICE = (
('Square', 'Square'),
('Round', 'Round')
)



class Product(models.Model):
    eid = models.AutoField(primary_key=True)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=50, default="")
    piztype = models.CharField(choices=TYPE_CHOICES, max_length=25, default="")
    shape = models.CharField(choices=SHAPE_CHOICE,max_length=20, default="")
    title = models.CharField(max_length=50)
    desc = models.TextField()
    mrp = models.IntegerField(default=0)
    image = models.ImageField(upload_to="pizzacart/images", default="")
    date = models.DateField()

    def __str__(self):
        return str(self.eid) + " " + self.title

    @staticmethod
    def get_product(li):
        return Product.objects.filter(eid__in=li)