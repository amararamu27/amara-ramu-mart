from django.db import models

class ProductModel(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=100,unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    photo = models.ImageField(upload_to='product_images/')

class CustomerModel(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True)
    address = models.TextField()
    password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="customer_images/")

class OrderModel(models.Model):
    oid = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(CustomerModel,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)


