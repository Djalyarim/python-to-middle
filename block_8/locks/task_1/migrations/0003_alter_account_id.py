# Generated by Django 3.2.13 on 2022-08-06 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locks_task_1', '0002_alter_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
