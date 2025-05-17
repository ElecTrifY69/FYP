from django.db import models
from Shopping.models.customer import Customer


class Profile(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    images = models.ImageField(default='static/UserProfile/user.png', upload_to='static/UserProfile')
    address = models.CharField(max_length=150, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.customer.first_name

    @staticmethod
    def get_profile_by_customer(customer_id):
        return Profile.objects.filter(customer=customer_id)