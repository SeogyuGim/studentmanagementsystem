# Generated by Django 3.1.1 on 2020-09-23 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_student', models.BooleanField(default=False)),
                ('is_professor', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('preferred_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='profile-images')),
                ('fb_profile_url', models.CharField(max_length=100)),
                ('twitter_profile_url', models.CharField(max_length=100)),
                ('linkedin_profile_url', models.CharField(max_length=100)),
                ('website_url', models.CharField(max_length=100)),
                ('current_level', models.IntegerField(choices=[(1, 'Level One'), (2, 'Level Two'), (3, 'Level Three'), (4, 'Level Four')])),
            ],
        ),
    ]
