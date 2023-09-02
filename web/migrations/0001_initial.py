# Generated by Django 4.2.3 on 2023-09-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField(max_length=755)),
                ('profile', models.ImageField(blank=True, upload_to='profile_images/')),
                ('house_no', models.CharField(blank=True, max_length=255)),
                ('street_address', models.CharField(blank=True, max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('zip_code', models.CharField(blank=True, max_length=20)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('email_verification_token', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]