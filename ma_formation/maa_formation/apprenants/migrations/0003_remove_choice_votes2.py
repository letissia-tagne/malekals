# Generated by Django 4.2.5 on 2023-10-18 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprenants', '0002_choice_votes2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='votes2',
        ),
    ]
