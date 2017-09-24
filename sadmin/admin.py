from django.contrib import admin
from .models import documenttype,uploadeddocuments,pickup,pickupdetails

admin.site.register(documenttype)
admin.site.register(uploadeddocuments)
admin.site.register(pickup)
admin.site.register(pickupdetails)


