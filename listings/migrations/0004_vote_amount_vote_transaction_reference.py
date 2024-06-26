# Generated by Django 5.0.4 on 2024-06-04 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_discipline_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='amount',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='vote',
            name='transaction_reference',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
