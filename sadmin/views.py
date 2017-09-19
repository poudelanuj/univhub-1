from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "base_generic.html")


def getPickup(request):
	return render(request, "pickup.html")