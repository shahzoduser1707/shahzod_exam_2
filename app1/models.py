from django.db import models
from datetime import datetime

# Create your models here.

class Ustalar(models.Model):
    usta_name = models.CharField(max_length=150,default='')
    usta_last_name = models.CharField(max_length=150,default='')
    date_of_birth = models.DateTimeField(default=datetime.now)
    status_available = models.BooleanField(default=False)
    

    class Meta:
        db_table = 'Ustalar'
    def __str__(self) -> str:
        return self.usta_name
    
class Orderlar(models.Model):
    order_name = models.CharField(max_length=200,default='')
    order_payment = models.IntegerField(default=0)
    description = models.TextField('you can type anything')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)
    ustalar = models.ForeignKey(Ustalar, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Orderlar'
    def __str__(self) -> str:
        return self.order_name

