# Generated by Django 4.2.13 on 2024-05-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("upload_app", "0002_photo_image_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="photo",
            name="image_url",
        ),
        migrations.AddField(
            model_name="photo",
            name="transformed_image",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="photo",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
