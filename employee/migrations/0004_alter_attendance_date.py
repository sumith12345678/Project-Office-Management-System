# Generated by Django 4.1.3 on 2023-04-04 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_task_task_pdf_alter_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 4, 20, 14, 14, 898591)),
        ),
    ]
