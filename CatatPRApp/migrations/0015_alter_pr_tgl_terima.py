# Generated by Django 4.2.16 on 2025-01-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatatPRApp', '0014_alter_pr_options_pr_tgl_terima'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pr',
            name='tgl_terima',
            field=models.DateField(blank=True, null=True),
        ),
    ]
