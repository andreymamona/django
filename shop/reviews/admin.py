from reviews.models import Article, Review

from django.contrib import admin


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "article",
        "review_title",
        "tags_in_review",
        "created_at",
    )
    fields = (
        "user",
        "product",
        "article",
        "review_title",
        "tags_in_review",
        "created_at",
    )
    readonly_fields = ("created_at",)
    search_fields = (
        "review_title",
        "user",
        "product",
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "review",
        "image",
        "review_text",
        "created_at",
    )
    fields = (
        "review",
        "image",
        "review_text",
        "created_at",
    )
    readonly_fields = ("created_at",)
    search_fields = (
        "review",
        "review_text",
    )
