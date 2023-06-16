from django.db import models
from django.contrib.auth.models import User
from django.conf import settings  # new




class Rally(models.Model):
    LEVELS = (('L1', 'Easy'), ('L2', 'Medium'), ('L3', 'Hard') )
    description = models.CharField(max_length=50, default='Lokalny rajd')
    date = models.DateField()
    time = models.TimeField(default='00:00:00')
    level = models.CharField(max_length=10, choices=LEVELS, default='L2')   #int
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.description


class ParticipantsList(models.Model):
    id_rally = models.ForeignKey(Rally, on_delete=models.CASCADE)
    id_participant = models.ForeignKey(User, on_delete=models.CASCADE)
    # id_participant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# class Ride(models.Model):
#     name = models.CharField(max_length=40)
#     distance = models.FloatField()
#     # total_time = models.DurationField()
#     total_time = models.FloatField()
#     # start_date = models.DateTimeField(auto_now_add=True)
#     start_date = models.DateTimeField()
#     max_speed = models.FloatField()
#     # min_elevation = models.FloatField()
#     # max_elevation = models.FloatField()
#     moving_time = models.FloatField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)