# Generated by Django 5.1.5 on 2025-01-20 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditdetailsmodel',
            name='credit_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchase_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
