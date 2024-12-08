from django.db import models

class Price(models.Model):
    price = models.IntegerField(verbose_name='Price')
    created_time = models.DateTimeField(auto_now_add=True)