# Generated by Django 4.0.1 on 2022-01-28 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner'), ('snacks', 'snacks')], max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fooditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('carbonhydrate', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('fats', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('calorie', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5)),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('category', models.ManyToManyField(to='Fityfeed.Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserFooditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ManyToManyField(blank=True, to='Fityfeed.Customer')),
                ('fooditem', models.ManyToManyField(to='Fityfeed.Fooditem')),
            ],
        ),
    ]
