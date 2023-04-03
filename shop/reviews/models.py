from django.db import models
from django.conf import settings
from django.db.models import ImageField


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews"
    )
    product = models.ManyToManyField("products.Product", related_name="reviews")
    article = models.OneToOneField(
        "reviews.Article", on_delete=models.CASCADE, related_name="reviews", blank=True, null=True
    )
    review_title = models.CharField(max_length=255)
    tags_in_review = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)


class Article(models.Model):
    review = models.OneToOneField(
        "reviews.Review", on_delete=models.CASCADE, related_name="articles"
    )
    image = ImageField(upload_to="reviews/", blank=True, null=True)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
