# Generated by Django 5.0.3 on 2024-03-20 11:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_appointment_doctor_alter_appointment_patient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_time',
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_start', models.DateTimeField()),
                ('timestamp_end', models.DateTimeField()),
                ('appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedules', to='api.appointment')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedules', to='api.doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedules', to='api.patient')),
            ],
        ),
    ]
