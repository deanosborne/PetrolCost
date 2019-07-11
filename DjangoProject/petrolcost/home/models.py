from django.db import models
from django.contrib.auth.models import User

class Partner(models.Model):

    PROVIDER_CHOICES =(
        ('','BP'), ('','Mobil'),
        ('','NPD'), ('','Challenge'),
        ('', 'Caltex'), ('','Z')
    )

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=50)
    provider = models.CharField(choices=PROVIDER_CHOICES, max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.provider

class Deal(models.Model):

    partner = models.ForeignKey('Partner', on_delete=models.SET_NULL, null=True, blank=True)
    consumer = models.ForeignKey('Consumer', on_delete=models.SET_NULL, null=True, blank=True)
    deal_name = models.CharField(max_length=50)
    deal_url = models.CharField(max_length=50)
    deal_descrip = models.TextField()

    def __str__(self):
        return self.deal_name

class Consumer(models.Model):

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
