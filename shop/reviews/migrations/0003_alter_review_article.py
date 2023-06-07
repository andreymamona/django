# Generated by Django 4.1.7 on 2023-04-03 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0002_article_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="article",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="reviews.article",
            ),
        ),
    ]
