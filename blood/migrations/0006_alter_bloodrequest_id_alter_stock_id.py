# Generated by Django 5.1.2 on 2024-10-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0005_alter_bloodrequest_id_alter_stock_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
