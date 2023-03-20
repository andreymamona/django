from django.conf import settings
from django.db import models

COLOR_CHOICES = (
    ("RED", "Red"),
    ("GREEN", "Green"),
    ("BLUE", "Blue"),
    ("BLACK", "Black"),
    ("WHITE", "White"),
    ("BROWN", "Brown"),
    ("YELLOW", "Yellow"),
    (None, None),
)


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=32, choices=COLOR_CHOICES, default=None)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )

    def __str__(self):
        return f'Product: {self.title} Price: {self.price}'

    def get_field_data(self):
        datalist = []
        for field in self._meta.get_fields():
            if field.name != 'id' and field.name != 'created_at':
                datalist.append(getattr(self, field.name))
        return datalist


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="purchases"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="purchases"
    )
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
