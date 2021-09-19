from django.contrib import admin
from .models import Laptop

class LaptopAdmin(admin.ModelAdmin):
    list_display=['id','name','company','ram','rom','price','processor']
admin.site.register(Laptop,LaptopAdmin)    
