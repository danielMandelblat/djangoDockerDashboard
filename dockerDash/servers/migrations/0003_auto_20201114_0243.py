# Generated by Django 3.1.3 on 2020-11-14 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0002_auto_20201113_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='Server_id',
            new_name='Server_ID',
        ),
    ]