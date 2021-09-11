from django.db import models

# Create your models here.
class product(models.Model): 
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category= models.CharField(max_length=50, default="")
    subcategory= models.CharField(max_length=50, default="")
    price = models.IntegerField( default="0")
    Warranty = models.CharField(max_length=100, default="1 Year Manufacturing Domestic Warranty ")
    brand= models.CharField(max_length=50, default="")
    color= models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=1000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="ecom/images", default="")
    

    def __str__(self):
        return self.product_name

class contact(models.Model): 
    msgid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=70, default="")
    phone= models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=5000, default="")
    

    def __str__(self):
        return self.name