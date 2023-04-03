from django.contrib import admin
from reviews.models import Review, Article
from products.models import Product


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "article", "review_title", "tags_in_review", "created_at",)
    fields = ("user", "product", "article", "review_title", "tags_in_review", "created_at",)
    readonly_fields = ("created_at",)
    search_fields = ("review_title", "user", "product",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("review", "image", "review_text", "created_at",)
    fields = ("review", "image", "review_text", "created_at",)
    readonly_fields = ("created_at",)
    search_fields = ("review", "review_text",)

