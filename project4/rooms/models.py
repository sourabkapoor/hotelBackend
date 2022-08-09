from django.db import models

# Create your models here.
class Rooms(models.Model):
    room_number = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    availability = models.BooleanField()
    sea_view = models.BooleanField()
    pool_view = models.BooleanField()

    def __str__(self):
        return "room %s" % (self.room_number)