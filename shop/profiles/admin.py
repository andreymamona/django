from django.contrib import admin

from profiles.models import Profile
from profiles.models import Address


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "age", "created_at")
    fields = ("user", "first_name", "last_name", "age", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("first_name", "last_name", "age")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "city",
        "street",
        "building_number",
        "appartment",
        "created_at",
    )
    fields = ("user", "city", "street", "building_number", "appartment", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user__email", "user__profile__last_name", "city", "street")
