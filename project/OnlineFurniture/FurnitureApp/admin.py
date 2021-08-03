from django.contrib import admin
from FurnitureApp1.models import OnlineFurniture,FitemList,Product,Category
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['pname', 'price', 'category']



class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(OnlineFurniture)
admin.site.register(FitemList)
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)

