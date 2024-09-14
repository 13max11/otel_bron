from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    number = models.IntegerField()
    capacyty = models.IntegerField()
    location = models.TextField()
    discription = models.TextField()

    def __str__(self):
        return f'{self.number} - {self.location}'

    class Meta:
        ordering = ['number', 'location']

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.room.number} - {self.room.location}"