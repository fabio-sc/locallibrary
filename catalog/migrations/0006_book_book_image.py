# Generated by Django 3.0.5 on 2020-04-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200331_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(blank=True, upload_to='book-images/'),
        ),
    ]