# Generated by Django 3.0.6 on 2021-09-27 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20210925_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('message_to_buyer', models.TextField()),
            ],
        ),
    ]
