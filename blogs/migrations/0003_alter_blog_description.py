# Generated by Django 4.2.5 on 2023-10-18 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_rename_image_blog_image1_remove_blog_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=555),
        ),
    ]
