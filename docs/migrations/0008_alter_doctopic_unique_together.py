# Generated by Django 4.0 on 2022-01-07 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0007_alter_doctopic_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='doctopic',
            unique_together=set(),
        ),
    ]
