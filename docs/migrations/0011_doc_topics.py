# Generated by Django 4.0 on 2022-01-07 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0010_alter_doctopic_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='topics',
            field=models.ManyToManyField(through='docs.DocTopic', to='docs.Topic'),
        ),
    ]