# Generated by Django 5.1 on 2024-09-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0014_networth_savingexpense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savingexpense',
            name='purpose',
            field=models.CharField(max_length=250),
        ),
    ]
