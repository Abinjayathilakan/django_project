# Generated by Django 4.1.7 on 2023-04-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0004_alter_usermember_course_alter_usermember_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermember',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
