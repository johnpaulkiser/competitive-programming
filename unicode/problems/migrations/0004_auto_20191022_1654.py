# Generated by Django 2.2.5 on 2019-10-22 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_auto_20191017_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem',
            old_name='submitted',
            new_name='user',
        ),
    ]
