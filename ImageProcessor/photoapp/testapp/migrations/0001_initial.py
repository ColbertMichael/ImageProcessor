# Generated by Django 5.1.1 on 2024-10-06 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myfilefield', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
