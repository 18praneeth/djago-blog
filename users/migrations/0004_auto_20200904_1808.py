# Generated by Django 3.1.1 on 2020-09-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200904_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.PositiveBigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[(False, 'Mentee'), (True, 'Mentor')], default=False, max_length=10),
        ),
    ]
