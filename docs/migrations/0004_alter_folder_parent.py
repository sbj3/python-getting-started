# Generated by Django 4.0 on 2022-01-06 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_alter_doc_options_alter_doc_folder_alter_doc_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='docs.folder'),
        ),
    ]