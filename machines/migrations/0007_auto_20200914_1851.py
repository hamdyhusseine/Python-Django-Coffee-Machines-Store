# Generated by Django 3.1.1 on 2020-09-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0006_auto_20200914_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeemachine',
            name='Category',
            field=models.CharField(blank=True, choices=[('Base', 'Base'), ('Premium', 'Premium'), ('Deluxe', 'Deluxe')], max_length=50),
        ),
        migrations.AlterField(
            model_name='coffeemachine',
            name='coffee_flavor',
            field=models.CharField(blank=True, choices=[('Coffee Flavor Vanilla', 'Coffee Flavor Vanilla'), ('Coffee Flavor Caramel', 'Coffee Flavor Caramel'), ('Coffee Flavor Psl', 'Coffee Flavor Psl'), ('Coffee Flavor Mocha', 'Coffee Flavor Mocha'), ('Coffee Flavor Hazelunt', 'Coffee Flavor Hazelunt')], max_length=50),
        ),
        migrations.AlterField(
            model_name='coffeemachine',
            name='product_type',
            field=models.CharField(blank=True, choices=[('Large Machine', 'Large Machine'), ('Small Machine', 'Small Machine'), ('Espresso Machine', 'Espresso Machine')], max_length=50),
        ),
        migrations.AlterField(
            model_name='coffeemachine',
            name='product_type_pods',
            field=models.CharField(blank=True, choices=[('Coffee Pod Large', 'Coffee Pod Large'), ('Coffee Pod Small', 'Coffee Pod Small'), ('Espresso Pod', 'Espresso Pod')], max_length=50),
        ),
    ]
