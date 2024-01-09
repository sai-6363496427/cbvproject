from django.db import models
from django.urls import reverse


# Create your models here.
class company(models.Model):
    c_name = models.CharField(max_length=200)
    ceo = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)

    def __str__(self):
        return self.c_name
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class foodprod(models.Model):
    prd_name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    manufact_date = models.DateField()
    exp_date = models.DateField()
    company = models.ForeignKey(company,related_name="companies",on_delete=models.CASCADE)

    def __str__(self):
        return self.prd_name
    
    