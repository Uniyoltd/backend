# Generated by Django 4.1.7 on 2023-03-16 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_user_address'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(null=True, upload_to='')),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('transport_per_km', models.DecimalField(decimal_places=2, max_digits=6)),
                ('availability', models.CharField(max_length=255)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='booking_unit.business')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='booking_unit.service')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='booking_unit.service')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
                ('photo', models.CharField(max_length=255)),
                ('video', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('delivery_at', models.DateTimeField(null=True)),
                ('duration_in_hours', models.FloatField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_at', models.DateTimeField(auto_now=True)),
                ('delivery_at', models.DateTimeField(null=True)),
                ('duration_in_hours', models.FloatField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('transport_per_km', models.DecimalField(decimal_places=2, max_digits=6)),
                ('address', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('S', 'Paid'), ('C', 'Completed')], default='P', max_length=1)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='buyers', to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='booked_services', to='booking_unit.service')),
            ],
        ),
    ]
