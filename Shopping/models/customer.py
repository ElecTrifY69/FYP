from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    username = models.CharField(max_length=150, )
    email = models.EmailField(null=True)
    password = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    images = models.ImageField(default='static/UserProfile/user.png', upload_to='static/UserProfile', blank=True,
                               null=True)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def register(self):
        self.save()

    def __str__(self):
        return self.first_name + self.last_name

    @staticmethod
    def get_all_customers():
        return Customer.objects.all()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_customer_by_id(id):
        try:
            return Customer.objects.get(id=id)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
            return False

    def userisExists(self):
        if Customer.objects.filter(username=self.username):
            return True
            return False

    def phoneisExists(self):
        if Customer.objects.filter(phone=self.phone):
            return True
            return False

    @staticmethod
    def get_customers_by_customer(customer_id):
        return Customer.objects.get(customer=customer_id)
