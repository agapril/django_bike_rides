from django.db import models
from django.contrib.auth.models import User
from django.conf import settings  # new


class Ride(models.Model):
    name = models.CharField(max_length=40)
    distance = models.FloatField()
    # total_time = models.DurationField()
    total_time = models.FloatField()
    # start_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    max_speed = models.FloatField()
    # min_elevation = models.FloatField()
    # max_elevation = models.FloatField()
    moving_time = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
