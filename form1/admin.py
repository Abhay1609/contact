from django.contrib import admin

# Register your models here.
from .models import contact_form
@admin.register(contact_form)
class contact(admin.ModelAdmin):
    list_display=['id','name','surname','email']