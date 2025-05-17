from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=350)


    def __str__(self):
        return self.name
