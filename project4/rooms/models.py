from django.db import models

# Create your models here.
class Rooms(models.Model):
    room_number = models.CharField(max_length=30, primary_key=True)
    price = models.CharField(max_length=30)
    availability = models.BooleanField(default=True)
    sea_view = models.BooleanField(default=False)
    pool_view = models.BooleanField(default=False)

    def __str__(self):
        return "room %s" % (self.room_number)