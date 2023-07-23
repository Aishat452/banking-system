# Generated by Django 4.2.2 on 2023-07-23 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email address')),
                ('fullname', models.CharField(max_length=255, unique=True, verbose_name='full name')),
                ('user_address', models.CharField(max_length=255)),
                ('user_address2', models.CharField(max_length=255)),
                ('user_city', models.CharField(max_length=255)),
                ('user_state', models.CharField(max_length=255)),
                ('user_zipcode', models.CharField(max_length=10)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('date_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
