# Generated by Django 4.2.7 on 2023-12-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0010_zaved_type_bookingtablezaved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zaved',
            name='description',
        ),
        migrations.AddField(
            model_name='zaved',
            name='adress',
            field=models.TextField(default='null', verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaved',
            name='avr_cost',
            field=models.TextField(default='null', verbose_name='Средний счет'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaved',
            name='children',
            field=models.TextField(default='null', verbose_name='Что есть для Детей'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaved',
            name='count_people',
            field=models.TextField(default='null', verbose_name='Количество мест'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaved',
            name='desc_zal',
            field=models.TextField(default='null', verbose_name='Описание зала'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaved',
            name='have',
            field=models.TextField(default='null', verbose_name='Есть в зале'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaved',
            name='kitchen',
            field=models.TextField(default=1, verbose_name='Кухня'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaved',
            name='more_desc',
            field=models.TextField(default='null', verbose_name='Полное описание заведения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaved',
            name='music',
            field=models.TextField(default='null', verbose_name='Музыка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaved',
            name='parking',
            field=models.TextField(default='null', verbose_name='Парковка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaved',
            name='site_adress',
            field=models.TextField(default='null', verbose_name='Веб сайт ресторана (если нет -)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaved',
            name='sotial',
            field=models.TextField(default='null', verbose_name='Социальная сеть (если нет -)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaved',
            name='telephone',
            field=models.TextField(default='null', verbose_name='номер телефона (если нет -)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaved',
            name='time_work',
            field=models.TextField(default='null', verbose_name='Время работы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zaved',
            name='whatsapp',
            field=models.TextField(default='null', verbose_name='Ватцап номер (если нет -)'),
            preserve_default=False,
        ),
    ]