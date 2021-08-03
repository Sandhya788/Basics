from django.contrib import admin
from FurnitureApp1.models import Restaurant,Restaurantlist
# Register your models here.

# class AdminProduct(admin.ModelAdmin):
#     list_display = ['pname', 'price', 'category']



# class AdminCategory(admin.ModelAdmin):
#     list_display = ['name']

admin.site.register(Restaurant)
admin.site.register(Restaurantlist)
# admin.site.register(Product,AdminProduct)
# admin.site.register(Category,AdminCategory)

