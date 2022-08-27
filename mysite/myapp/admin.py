from django.contrib import admin

from myapp.models import Car, Dealer
# from .models import  Musician

# # Register your models here.
# admin.site.register(Musician)
# admin.site.register(Student)
# admin.site.register(TablespaceEx)
# class CarAdmin(admin.ModelAdmin):
#     list_display = ['name_id','name','car_img','specs']
admin.site.register(Car)

# class DealerAdmin(admin.ModelAdmin):
#     list_display=['dealer_id','dealer_name']
admin.site.register(Dealer)