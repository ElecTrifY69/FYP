from django.contrib import admin
from .models.contact import Contact
from .models.review import Review


# Register your models here.
class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'subject', 'message']
    list_filter = ['name', 'email']


class AdminReview(admin.ModelAdmin):
    list_display = ['fullname', 'message']
    list_filter = ['fullname']


admin.site.register(Contact, AdminContact)
admin.site.register(Review, AdminReview)
