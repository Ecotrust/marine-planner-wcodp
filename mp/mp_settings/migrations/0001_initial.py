# Generated by Django 2.2.3 on 2019-07-03 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarinePlannerSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, help_text='Only 1 project can be active at any time.')),
                ('project_name', models.CharField(blank=True, help_text='If there is no entry for Project Logo, your Project Name will be displayed at the top-left of the screen.', max_length=75, null=True)),
                ('slug_name', models.CharField(blank=True, help_text='This Slug Name can be used in the URL to distinguish one project from another (/my_slug/planner or /my_slug/catalog).', max_length=75, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('zoom', models.IntegerField(blank=True, null=True)),
                ('min_zoom', models.IntegerField(blank=True, default=5, help_text='Minimum Zoom Level (5 is default).', null=True)),
                ('max_zoom', models.IntegerField(blank=True, default=12, help_text='Maximum Zoom Level (12 is default).', null=True)),
                ('project_logo', models.CharField(blank=True, help_text='Either a relative path within your media directory or a valid URL.', max_length=255, null=True)),
                ('project_icon', models.CharField(blank=True, help_text='Either a relative path within your media directory or a valid URL.', max_length=255, null=True)),
                ('project_home_page', models.URLField(blank=True, help_text='The Project Name or Project Logo will link to this page.', max_length=255, null=True)),
                ('bitly_registered_domain', models.URLField(blank=True, max_length=255, null=True)),
                ('bitly_username', models.CharField(blank=True, max_length=75, null=True)),
                ('bitly_api_key', models.CharField(blank=True, max_length=75, null=True)),
                ('table_of_contents', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_manager.TOC')),
            ],
        ),
    ]
