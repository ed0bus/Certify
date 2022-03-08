from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Certificate(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255, null=True)
    birth_date = models.DateField()
    subject = models.CharField(max_length=255)
    achievement_date = models.DateField()
    certificate_score = models.IntegerField(default=1, validators=[MaxValueValidator(30), MinValueValidator(0)])
    issuance_date = models.DateTimeField(default=timezone.now)
    hash = models.CharField(max_length=66, default=None, null=True, blank=True)
    txId = models.CharField(max_length=66, default=None, null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.surname


class AdminIP(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True)
