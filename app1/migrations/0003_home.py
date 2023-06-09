# Generated by Django 4.1 on 2022-10-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0002_features"),
    ]

    operations = [
        migrations.CreateModel(
            name="Home",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(max_length=50)),
                ("more_name", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("shoes_image", models.ImageField(upload_to="upload/images")),
                ("image2", models.ImageField(upload_to="upload/images")),
            ],
        ),
    ]
