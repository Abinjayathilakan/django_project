# Generated by Django 4.1.7 on 2023-04-12 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_app', '0002_studentdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usermember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('number', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
