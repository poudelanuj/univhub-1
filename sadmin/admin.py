from django.contrib import admin
from .models import *

# class RentalAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
#     }

admin.site.register(District)
admin.site.register(ApplyType)
admin.site.register(ProgramsOffered)
admin.site.register(Country)

admin.site.register(UserProfile)
admin.site.register(pickup)
admin.site.register(SubMajor)
admin.site.register(Tutor)
admin.site.register(ClassType)
admin.site.register(OfferedClass)
admin.site.register(RegisteredClass)
admin.site.register(OfferType)
admin.site.register(Offer)
admin.site.register(Universities)

# admin.site.register(UserProfile)
# admin.site.register(UserProfile)

admin.site.register(deliveryMan)
admin.site.register(documenttype)
admin.site.register(documentfor)
admin.site.register(uploadeddocuments)
admin.site.register(pickupdetails)
admin.site.register(scheduledpickup)