# Generated by Django 4.2.3 on 2023-07-12 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="image",
            field=models.ImageField(null=True, upload_to="images/"),
        ),
    ]
