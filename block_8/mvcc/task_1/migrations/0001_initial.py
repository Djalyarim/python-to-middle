# Generated by Django 3.2.13 on 2022-07-24 11:02

from django.db import migrations, models, connection



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField(verbose_name='Дата регистрации')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('rating', models.IntegerField(default=0, verbose_name='Рейтинг')),
            ],
            options={
                'db_table': 'mvcc_customer',
            },
        ),

    ]
