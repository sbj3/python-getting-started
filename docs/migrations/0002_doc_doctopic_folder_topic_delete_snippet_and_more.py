# Generated by Django 4.0 on 2022-01-05 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('document', models.BinaryField()),
                ('folder', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='docs', to='auth.user')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='DocTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('doc_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='docs.doc')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='doctopics', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='folders', to='auth.user')),
                ('parent', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='docs.folder')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_desc', models.CharField(
                    blank=True, default='', max_length=100)),
                ('description', models.CharField(
                    blank=True, default='', max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='auth.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
        migrations.AddField(
            model_name='doctopic',
            name='topic_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='docs.topic'),
        ),
    ]