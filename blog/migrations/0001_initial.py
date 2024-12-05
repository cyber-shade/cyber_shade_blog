# Generated by Django 5.1.3 on 2024-12-05 12:36

import django.contrib.postgres.fields
import django.db.models.deletion
import django_ckeditor_5.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('cover', models.ImageField(upload_to='covers')),
                ('text', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('views', models.PositiveIntegerField(default=0)),
                ('special', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('resources', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255, unique=True), blank=True, null=True, size=None)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('tags', models.ManyToManyField(blank='true', related_name='blogs', to='core.tag')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
