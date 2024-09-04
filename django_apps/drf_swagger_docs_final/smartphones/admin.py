from django.contrib import admin
from .models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("name", "manufacturer", "year")
    search_fields  = ("name", "manufacturer", "year")
    list_filter = ("manufacturer", "year", "operating_system")
