# Generated by Django 4.2 on 2023-05-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderName', models.CharField(max_length=510)),
                ('orderaddress', models.CharField(max_length=515)),
                ('orderemail', models.CharField(max_length=515)),
                ('orderphone', models.IntegerField()),
                ('items', models.CharField(max_length=44)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('delivery', models.BooleanField(default=False)),
            ],
        ),
    ]
