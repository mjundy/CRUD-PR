# Generated by Django 4.2.16 on 2024-11-07 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl_pr', models.DateField(max_length=255, null=True)),
                ('partnumber', models.CharField(max_length=255, unique=True)),
                ('partname', models.CharField(max_length=255)),
                ('qty', models.IntegerField()),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('delete', models.BooleanField(default=False)),
            ],
        ),
    ]