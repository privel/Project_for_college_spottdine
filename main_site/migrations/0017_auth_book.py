# Generated by Django 4.2.7 on 2023-12-28 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0016_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='main_site.bookingtable'),
        ),
    ]