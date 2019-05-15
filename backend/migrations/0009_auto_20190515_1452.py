# Generated by Django 2.1.7 on 2019-05-15 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20190515_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition_results',
            name='team',
        ),
        migrations.AddField(
            model_name='competition_results',
            name='regist_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='backend.RegisterInfo'),
        ),
    ]