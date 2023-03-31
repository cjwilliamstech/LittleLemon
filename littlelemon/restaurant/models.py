from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    # id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length= 255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()
    
class Menu(models.Model):
    # id = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length= 255)
    Price = models.DecimalField(max_digits= 6, decimal_places= 2)
    Inventory = models.SmallIntegerField()
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    
# class User(models.User):
    
    
    
    
    