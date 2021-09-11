# Generated by Django 3.0.5 on 2020-09-12 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_auto_20200827_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('msgid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=5000)),
            ],
        ),
    ]
