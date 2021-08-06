from django.db import models

class Person(models.Model):
    name = models.CharField("Contact name", max_length=50)

    def __str__(self):
        return self.name

class Phone(models.Model):
    phone = models.CharField("Phone number", max_length=50)
    contact = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="phone")
    def __str__(self):
        return self.phone