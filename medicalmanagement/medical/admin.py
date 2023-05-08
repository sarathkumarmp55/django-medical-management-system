from django.contrib import admin
from .models import contact,medicine,order

# Register your models here.
admin.site.register(contact)
admin.site.register(medicine)
admin.site.register(order)