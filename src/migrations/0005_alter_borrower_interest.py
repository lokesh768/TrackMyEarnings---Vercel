# Generated by Django 5.1 on 2024-09-13 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_alter_borrower_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='interest',
            field=models.CharField(max_length=10),
        ),
    ]
