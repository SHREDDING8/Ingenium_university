# Generated by Django 3.0 on 2021-09-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_delete_lendinghome'),
    ]

    operations = [
        migrations.CreateModel(
            name='LendingHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='имя', max_length=50, verbose_name='имя')),
                ('phone', models.CharField(help_text='телефон', max_length=12, verbose_name='телефон')),
                ('email', models.EmailField(help_text='email', max_length=254, verbose_name='email')),
                ('date', models.DateTimeField(auto_now=True, help_text='дата', verbose_name='дата')),
            ],
            options={
                'verbose_name': 'Лендинг',
                'verbose_name_plural': 'Лендинг',
            },
        ),
    ]
