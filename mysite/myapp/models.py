# from datetime import date
# from email.policy import default
# from tkinter.tix import Tree
# from configparser import MAX_INTERPOLATION_DEPTH
import uuid
from django.db import models
# from django.contrib.auth.models import User
# from django.utils.translation import gettext_lazy as _
# from django.core.exceptions import ValidationError

# Create your models here.
# class Musician(models.Model):
#     first_name  = models.CharField(max_length=50,  verbose_name='Enter your name')
#     last_name   = models.CharField(max_length=50)
#     instrument  = models.CharField(max_length=50, null=True)
    
#     def __str__(self):
#         return self.first_name

# Intern = "IN"
# Fresher = "FR"
# Experience = "EX"

# exp_in_comp_choices=[
#     (Fresher,"fresher"),
#     (Experience,"experience"),
#     (Intern,'intern'),
# ]
# today i will work on views
#asdfasdfsaf
# class Page(models.Model):
    
#     user = models.ManyToManyField(User,blank=True,null=True)
#     page_name = models.CharField(max_length=200,choices=exp_in_comp_choices, default=Intern)
#     page_cat = models.CharField(max_length=200)
#     page_pub_date = models.DateField()

#     def __str__(self):
#         return self.page_name       


# Enumirate
# class Student(models.Model):
#     class YearinSchool(models.IntegerChoices):
#         Fresher   =1
#         Experience=6
#         Intern    =4
#     Year_in_School=models.IntegerField(choices=YearinSchool.choices )

# Enumrate Tbalespace
# def validate_even(value):
#     if value % 2 != 0:
#         raise ValidationError(
#             _('%(value)s is not an even number'),
#             params={'value': value},
#         )



# class TablespaceEx(models.Model):
#     name = models.CharField(max_length=30, db_column=False)
#     data = models.IntegerField(validators=[validate_even])
#     shortcut = models.CharField(max_length=7)
#     edges = models.ManyToManyField(User)

#     class Meta:
#         db_tablespace = "tables"
#         indexes = [models.Index(fields=['name'], db_tablespace='indexes')]


# Feilds

# class Narayan(models.Model):
#     name_id =models.BigAutoField(primary_key=True)
#     name    =models.CharField(max_length=20, unique=True)
#     desh    =models.DecimalField(max_digits=5, decimal_places=3)


class Car(models.Model):
    id     = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name   =  models.CharField(max_length=20)
    car_img= models.ImageField(upload_to='car_img')
    specs  = models.FileField(upload_to='specs')
    
    def __str__(self):
        return f'{self.name} {self.specs}'

class Dealer(models.Model):
    cars       = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='Dealers')
    dealer_name= models.CharField(max_length=20)
    