# Generated by Django 4.2.16 on 2025-02-03 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CatatPRApp', '0025_alter_pr_sent_to_purchase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pr',
            old_name='sent_to_purchase',
            new_name='tgl_sent_to_purchase',
        ),
    ]
