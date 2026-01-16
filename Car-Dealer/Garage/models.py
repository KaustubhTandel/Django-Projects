from django.db import models


# Create your models here.

class Login(models.Model):
    Username=models.CharField( max_length=50)
    Password=models.CharField( max_length=50)


    
class Personal_Informations(models.Model):
    Name=models.CharField(max_length=20)
    Contact=models.IntegerField()
    Age=models.IntegerField()
    Gender=models.CharField(max_length=8)
    Email=models.EmailField(max_length=254)
    Address=models.CharField(max_length=80)

    class Meta:
        verbose_name_plural = "Personal_Informations"

    def __str__(self):
        return self.Name

class Car_Collections(models.Model):
    Car_Name=models.CharField( max_length=50)
    Model_Name=models.CharField( max_length=50)
    Car_Colour=models.CharField( max_length=50)

    def __str__(self):
        return self.Car_Name



class Payment(models.Model):
    Card_Number=models.IntegerField()
    Valid_Card_Date=models.DateField( auto_now=True)
    Expired_Card_Date=models.DateField( auto_now=True)
    CV_Number=models.CharField( max_length=50)

    def __str__(self):
        return f"{self.Card_Number}"