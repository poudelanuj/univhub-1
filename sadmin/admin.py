from django.contrib import admin
from .models import *

admin.site.register(documenttype)
admin.site.register(uploadeddocuments)
admin.site.register(pickup)
admin.site.register(pickupdetails)
admin.site.register(deliveryMan)
admin.site.register(scheduledpickup)
admin.site.register(documentfor)