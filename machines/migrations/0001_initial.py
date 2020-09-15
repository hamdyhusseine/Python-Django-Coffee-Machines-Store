# Generated by Django 3.1.1 on 2020-09-14 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='CoffeeMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=50)),
                ('product_type', models.CharField(blank=True, choices=[('COFFEE_MACHINE_LARGE', 'Large Machine'), ('COFFEE_MACHINE_SMALL', 'Small Machine'), ('ESPRESSO_MACHINE', 'Espresso Machine')], max_length=50)),
                ('water_line_compatible', models.BooleanField(blank=True, default=False)),
                ('product_type_pods', models.CharField(blank=True, choices=[('COFFEE_POD_LARGE', 'Coffee Pod Large'), ('COFFEE_POD_SMALL', 'Coffee Pod Small'), ('ESPRESSO_Pod', 'Espresso Pod')], max_length=50)),
                ('coffee_flavor', models.CharField(blank=True, choices=[('COFFEE_FLAVOR_VANILLA', 'Coffee Flavor Vanilla'), ('COFFEE_FLAVOR_CARAMEL', 'Coffee Flavor Caramel'), ('COFFEE_FLAVOR_PSL', 'Coffee Flavor Psl'), ('COFFEE_FLAVOR_MOCHA', 'Coffee Flavor Mocha'), ('COFFEE_FLAVOR_HAZELNUT', 'Coffee Flavor Hazelunt')], max_length=50)),
                ('PACKAGE_SIZE', models.CharField(blank=True, choices=[('1 dozen (12)', '1 dozen (12)'), ('3 dozen (36)', '3 dozen (36)'), ('5 dozen (60)', '5 dozen (60)'), ('7 dozen (84)', '7 dozen (84)')], max_length=50)),
                ('model_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.category')),
            ],
        ),
    ]
