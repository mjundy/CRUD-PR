# Generated by Django 4.2.16 on 2024-11-20 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatatPRApp', '0007_alter_pr_deskripsi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pr',
            name='partnumber',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
