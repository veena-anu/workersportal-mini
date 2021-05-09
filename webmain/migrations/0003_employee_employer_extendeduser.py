# Generated by Django 3.1.7 on 2021-05-02 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('webmain', '0002_delete_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('name', models.CharField(default='', max_length=255)),
                ('phnumber', models.CharField(max_length=10)),
                ('qualification', models.CharField(max_length=1000)),
                ('job', models.CharField(max_length=2000)),
                ('pin', models.IntegerField()),
                ('address', models.CharField(max_length=20000)),
                ('experience', models.CharField(max_length=2000)),
                ('flink', models.CharField(max_length=2000)),
                ('wages', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('name', models.CharField(default='', max_length=255)),
                ('phnumber', models.CharField(max_length=10)),
                ('pin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='extendedUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('isEmployee', models.BooleanField(default=False)),
                ('isEmployer', models.BooleanField(default=False)),
                ('request_for', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]