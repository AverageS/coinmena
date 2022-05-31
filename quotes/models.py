from django.db import models


class Quote(models.Model):
    ticket = models.CharField(max_length=64, unique=True)
    price = models.DecimalField(max_digits=19, decimal_places=10, null=True)
    last_updated = models.DateTimeField(auto_now=True)