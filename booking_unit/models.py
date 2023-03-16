from django.db import models
from django.conf import settings

class Business(models.Model):
    owner = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(null=True)
    status  = models.CharField(max_length=255)


    def get_status(self):
        return self.status
    

    def set_status(self, status):
        self.status = status



class Service(models.Model):
    name = models.CharField(max_length=255)
    business = models.ForeignKey(to=Business, on_delete=models.CASCADE, related_name='services')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    transport_per_km = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.CharField(max_length=255)


class ServiceImage(models.Model):
    name = models.CharField(max_length=255)
    service = models.ForeignKey(to=Service, on_delete=models.CASCADE, related_name='photos')


class ServiceVideos(models.Model):
    name = models.CharField(max_length=255)
    service = models.ForeignKey(to=Service, on_delete=models.CASCADE, related_name='videos')


class Request(models.Model):
    customer = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customers')
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    photo = models.CharField(max_length=255)
    video = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    delivery_at = models.DateTimeField(null=True)
    duration_in_hours = models.FloatField(null=True)


class Booking(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('S', 'Paid'),
        ('C', 'Completed'),
    ]

    buyer = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='buyers')
    booked_at = models.DateTimeField(auto_now=True)
    delivery_at = models.DateTimeField(null=True)
    duration_in_hours = models.FloatField(null=True)
    service = models.ForeignKey(to=Service, on_delete=models.PROTECT, related_name='booked_services')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    transport_per_km = models.DecimalField(max_digits=6, decimal_places=2)
    address = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default=STATUS_CHOICES[0][0])