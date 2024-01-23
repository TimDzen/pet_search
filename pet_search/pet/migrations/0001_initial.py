# Generated by Django 5.0.1 on 2024-01-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('species', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=2)),
                ('gender', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('owner_contact', models.CharField(max_length=255)),
                ('lost', models.BooleanField(default=True)),
            ],
        ),
    ]
