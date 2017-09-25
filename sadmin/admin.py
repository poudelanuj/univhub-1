from django.contrib import admin

from .models import documenttype, uploadeddocuments, pickupdetails,pickup

admin.site.register(documenttype)
admin.site.register(uploadeddocuments)
admin.site.register(pickupdetails)
admin.site.register(pickup)




