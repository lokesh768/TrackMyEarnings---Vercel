# Generated by Django 5.1 on 2024-09-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0015_alter_savingexpense_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networth',
            name='net_worth',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='networth',
            name='total_expenses',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='networth',
            name='total_savings',
            field=models.IntegerField(),
        ),
    ]
