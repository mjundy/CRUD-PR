# Generated by Django 4.2.16 on 2024-11-11 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatatPRApp', '0002_alter_pr_tgl_pr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pr',
            name='delete',
            field=models.CharField(default=False, max_length=255),
        ),
    ]
