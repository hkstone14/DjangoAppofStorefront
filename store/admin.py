from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']  # It will display these two columns
    list_editable = ['price']  # It will allow to edit product price
    list_per_page = 10


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']

    ordering = ['first_name', 'last_name']
    list_per_page = 10

    def membership(self, customer):
        return customer.MEMBERSHIP_CHOICES[1][1]


admin.site.register(models.Collection)
