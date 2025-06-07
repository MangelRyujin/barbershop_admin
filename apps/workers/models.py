from django.db import models
from apps.accounts.models import CustomUser

    
class Reservation(models.Model):
    STATE = [
        ("1","reservado"),
        ("2","confirmado"),
        ("3","completado"),
        ("4","cancelado")
    ]
    worker = models.ForeignKey(CustomUser,on_delete=models.PROTECT,null=True,blank=True)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    state = models.CharField(choices=STATE,default="1")

    class Meta:
        verbose_name = "Reservación"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return self.name
    
    