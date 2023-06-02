from django.contrib import admin
from .models import Food_Categories, OrderForm, Sub

# Register your models here.
# class EventsDetails(admin.ModelAdmin):
#     list_display=('event_name','event_description','event_image')
# admin.site.register(Events,EventsDetails)

class Food_Table(admin.ModelAdmin):
    list_display=('foodcate_name','foodcate_des','foodcate_img')
admin.site.register(Food_Categories,Food_Table)

# class Sub_Table(admin.ModelAdmin):
#     list_display=('subfood_name','subfood_price','subfood_image')
# admin.site.register(Sub_Category,Sub_Table)

class Sub_Tables(admin.ModelAdmin):
    list_display=('sub_name','sub_price','sub_image')
admin.site.register(Sub,Sub_Tables)

admin.site.register(OrderForm)