# Generated by Django 4.0 on 2022-01-07 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0011_doc_topics'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='docs',
            field=models.ManyToManyField(through='docs.DocTopic', to='docs.Doc'),
        ),
    ]
