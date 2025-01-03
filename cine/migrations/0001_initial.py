# Generated by Django 5.1.3 on 2024-12-02 23:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='streaming',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('debut_year', models.IntegerField(blank=True, null=True)),
                ('original_writer', models.CharField(blank=True, max_length=255, null=True)),
                ('resume', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(default='cine/default.jpg', upload_to='cine/')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cine_actor', to='cine.actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cine_director', to='cine.director')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cine_genre', to='cine.genre')),
                ('producers', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cine_producers', to='cine.producer')),
                ('streaming', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cine_streaming', to='cine.streaming')),
            ],
        ),
    ]
