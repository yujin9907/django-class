# Generated by Django 3.2.4 on 2021-06-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
    ]