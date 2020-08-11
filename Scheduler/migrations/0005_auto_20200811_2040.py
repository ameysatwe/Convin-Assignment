# Generated by Django 3.1 on 2020-08-11 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Scheduler', '0004_auto_20200811_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tasktracker',
            name='task_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scheduler.task'),
        ),
    ]
