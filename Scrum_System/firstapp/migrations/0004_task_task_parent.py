# Generated by Django 3.1.7 on 2021-03-14 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_user_boards'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstapp.boards'),
        ),
    ]
