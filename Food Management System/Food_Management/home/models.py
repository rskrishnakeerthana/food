from distutils.command.upload import upload
from email.policy import default
from django.db import models
# Create your models here.

class Food_Categories(models.Model):
    foodcate_name=models.CharField(max_length=150)
    foodcate_des=models.TextField()
    foodcate_img=models.ImageField(upload_to="food_categories",null=True)

    def __str__(self):
        return self.foodcate_name

# class Sub_Category(models.Model):
#     subfood_name=models.CharField(max_length=150,default="")
#     subfood_price=models.FloatField(max_length=50,default="")
#     foodcate_name=models.ForeignKey(Food_Categories,on_delete=models.CASCADE)
#     subfood_image=models.ImageField(upload_to="sub_categories",null=True)    

class Sub(models.Model):
    sub_name=models.CharField(max_length=150,default="")
    sub_price=models.FloatField(max_length=50,default="")
    foodcate_name=models.ForeignKey(Food_Categories,on_delete=models.CASCADE)
    sub_image=models.ImageField(upload_to="sub_cate",null=True)

class OrderForm(models.Model):
    food_name=models.CharField(max_length=50,default=" ")
    food_quantity=models.IntegerField(max_length=20,default=" ")
    customer_email=models.CharField(max_length=100,default=" ")
    customer_Mobile=models.IntegerField(max_length=15,default=" ")
    message=models.TextField(default=" ")