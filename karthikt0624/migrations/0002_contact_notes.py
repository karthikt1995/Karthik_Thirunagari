# Generated by Django 4.2.6 on 2023-11-11 02:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("karthikt0624", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
    ]