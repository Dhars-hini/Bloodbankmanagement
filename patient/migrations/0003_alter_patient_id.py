# Generated by Django 5.1.2 on 2024-10-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
