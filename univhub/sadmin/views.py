from django.shortcuts import render

# Create your views here.

def index(request):
<<<<<<< HEAD
    return render(request, "base_generic.html")




# dffdsf
def getPickup(request):
	return render(request, "pickup.html")
=======
    return render(request, "admin-dashboard.html")
def notifications(request):
    return render(request,"notifications.html")
>>>>>>> c9dff66fe5a7849e0a09b637e2688330e9c337af
