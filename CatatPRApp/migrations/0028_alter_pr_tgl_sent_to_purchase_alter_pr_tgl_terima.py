# Generated by Django 4.2.16 on 2025-02-05 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatatPRApp', '0027_alter_pr_tgl_sent_to_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pr',
            name='tgl_sent_to_purchase',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pr',
            name='tgl_terima',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
