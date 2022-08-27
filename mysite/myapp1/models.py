
from django.db import models
# import uuid
# from myapp.models import Musician

# # Create your models here.
# class Album(models.Model):
#     artist_id    = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='Album')
#     name         = models.CharField(max_length=50)
#     release_date = models.DateField('release date')
#     num_star     = models.IntegerField()

#     def __str__(self):
#         return self.name
    
# class Car(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name= models.CharField(max_length=20)
#     car_img= models.ImageField(upload_to='car_img')
#     specs= models.FileField(upload_to='specs')
    
#     def __str__(self):
#         return f'{self.name} {self.specs}'

# class Dealer(models.Model):
#     dealer_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='Dealers')
#     dealer_name= models.CharField(max_length=20)