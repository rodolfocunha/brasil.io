# Generated by Django 3.1.1 on 2020-09-17 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_control', '0004_blockedrequest_status_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockedrequest',
            name='headers',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='blockedrequest',
            name='path',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='blockedrequest',
            name='query_string',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='blockedrequest',
            name='source_ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blockedrequest',
            name='status_code',
            field=models.PositiveSmallIntegerField(blank=True, default=429, null=True),
        ),
        migrations.AlterField(
            model_name='blockedrequest',
            name='user_agent',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
