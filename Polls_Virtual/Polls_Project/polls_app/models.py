from django.db import models
from django.db.models.deletion import CASCADE
import uuid


class Floor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Rep(models.Model):
    floor = models.ForeignKey(Floor, on_delete=CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.fname} {self.lname}'


class Electorate(models.Model):
    name = models.CharField(max_length=200)
    std_id = models.CharField(max_length=8)
    pass_key = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name + " " + str(self.pass_key)
