from django.contrib import admin
from .models import *


admin.site.register(District)
admin.site.register(ApplyType)
admin.site.register(ProgramsOffered)
admin.site.register(Country)

admin.site.register(UserProfile)
admin.site.register(Pickup)
admin.site.register(SubMajor)
admin.site.register(Major)
admin.site.register(Tutor)
admin.site.register(ClassType)
admin.site.register(OfferedClass)
admin.site.register(RegisteredClass)
admin.site.register(OfferType)
admin.site.register(Offer)
admin.site.register(University)


admin.site.register(Deliveryman)
admin.site.register(DocumentType)
admin.site.register(DocumentFor)
admin.site.register(UploadedDocument)
admin.site.register(PickupDetail)
admin.site.register(Scheduledpickup)
