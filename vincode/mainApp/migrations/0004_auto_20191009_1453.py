# Generated by Django 2.2.6 on 2019-10-09 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20191009_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='vincode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.Vincode'),
        ),
    ]
