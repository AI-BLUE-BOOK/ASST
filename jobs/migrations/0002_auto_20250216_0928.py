# Generated by Django 3.2.20 on 2025-02-16 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.CharField(max_length=24, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
