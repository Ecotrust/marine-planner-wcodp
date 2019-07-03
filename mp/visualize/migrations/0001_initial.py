# Generated by Django 2.2.3 on 2019-07-03 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('url_hash', models.CharField(max_length=2050)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='visualize_bookmark_related', to='contenttypes.ContentType')),
                ('sharing_groups', models.ManyToManyField(blank=True, editable=False, related_name='visualize_bookmark_related', to='auth.Group', verbose_name='Share with the following groups')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visualize_bookmark_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
