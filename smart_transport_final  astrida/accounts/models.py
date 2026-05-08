from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', _('Admin')
        CUSTOMER = 'CUSTOMER', _('Customer')
        DRIVER = 'DRIVER', _('Driver')

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER,
    )
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    def is_admin(self):
        return self.role == self.Role.ADMIN

    def is_customer(self):
        return self.role == self.Role.CUSTOMER

    def is_driver(self):
        return self.role == self.Role.DRIVER

    def __str__(self):
        return self.username
    
    