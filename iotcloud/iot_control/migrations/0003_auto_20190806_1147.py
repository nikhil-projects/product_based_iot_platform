# Generated by Django 2.2.2 on 2019-08-06 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iot_control', '0002_auto_20190805_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extendeduser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_num', models.IntegerField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='P4node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=50)),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('status1', models.CharField(default='off', max_length=7)),
                ('status2', models.CharField(default='off', max_length=7)),
                ('status3', models.CharField(default='off', max_length=7)),
                ('status4', models.CharField(default='off', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='P8node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=50)),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('status1', models.CharField(default='off', max_length=7)),
                ('status2', models.CharField(default='off', max_length=7)),
                ('status3', models.CharField(default='off', max_length=7)),
                ('status4', models.CharField(default='off', max_length=7)),
                ('status5', models.CharField(default='off', max_length=7)),
                ('status6', models.CharField(default='off', max_length=7)),
                ('status7', models.CharField(default='off', max_length=7)),
                ('status8', models.CharField(default='off', max_length=7)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]