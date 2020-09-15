# Generated by Django 3.1.1 on 2020-09-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0005_auto_20200914_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeemachine',
            name='model_category',
        ),
        migrations.AddField(
            model_name='coffeemachine',
            name='Category',
            field=models.CharField(blank=True, choices=[('BASE_MODEL', 'Base'), ('PREMIUM_MODEL', 'Premium'), ('DELUXE_MODEL', 'Deluxe')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]