# Generated by Django 3.1.6 on 2021-02-26 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('NOT_ACCEPTED', 'Not accepted'), ('ACCEPTED', 'Accepted'), ('IN_PROGRESS', 'In progress'), ('COMPLETED', 'Completed')], default='NOT_ACCEPTED', max_length=20),
        ),
    ]
