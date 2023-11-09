# Generated by Django 4.2.7 on 2023-11-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_location', models.CharField(max_length=100)),
                ('description_location', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Название места',
                'verbose_name_plural': 'Название места',
            },
        ),
    ]
