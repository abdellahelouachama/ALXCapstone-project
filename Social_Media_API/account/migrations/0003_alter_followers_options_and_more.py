# Generated by Django 5.1.2 on 2024-12-23 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='followers',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='followers',
            unique_together=set(),
        ),
    ]
