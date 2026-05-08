from django.db import models

from django.db import models

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Bus(models.Model):
    name = models.CharField(max_length=100)
    plate_number = models.CharField(max_length=20, unique=True)
    capacity = models.PositiveIntegerField()
    route = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='buses')  # Link to driver

    def __str__(self):
        return f"{self.name} ({self.route})"


from django.contrib.auth import get_user_model

class Ticket(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starting_point = models.CharField(max_length=100, blank=True, null=True)
    ending_point = models.CharField(max_length=100, blank=True, null=True)


    

    def __str__(self):
        return f"Ticket {self.id} for {self.bus.name} by {self.customer.username}"
    
class Payment(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name="payment")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Payment for Ticket {self.ticket.id} - {self.amount} USD"


