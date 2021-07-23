from django.db import models

# Create your models here.
# Lop san bay
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.city} ({self.code})"

# Lop chuyen bay
# Co khoa ngoai lien ket voi lop san bay
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self) -> str:
        return f"Fligh {self.id}: {self.origin} to {self.destination}"

# Lop hanh khach
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers") # Noi voi django rang hanh khach co rat nhieu chuyen bay lien quan den lop Flight

    def __str__(self) -> str:
        return f"{self.first} {self.last}"
