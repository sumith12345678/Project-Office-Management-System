# Generated by Django 4.1.3 on 2023-03-27 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=30)),
                ('e_past_work', models.TextField(null=True)),
                ('e_photo', models.ImageField(upload_to='image/')),
                ('e_resume', models.ImageField(upload_to='resume/')),
                ('e_phone_number', models.CharField(max_length=20, unique=True)),
                ('e_address', models.TextField()),
                ('e_gender', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fk_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.department')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
