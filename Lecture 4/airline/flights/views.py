import flights
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger
# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights" : Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight" : flight,
        "passengers" : flight.passengers.all(), # sau flight la related_name
        "non_passengers" : Passenger.objects.exclude(flights=flight).all() # Lay tat ca hanh khach khong co tren chuyen bay hien tai
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id) # Lay chuyen bay theo flight_id
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"])) # Lay hanh khach theo thong tin tu form cua nguoi dung
        passenger.flights.add(flight) # Them chuyen bay vao chuyen bay cua hanh khach
        return HttpResponseRedirect(reverse("flight", args=(flight_id, ))) # Tra lai trang ban dau