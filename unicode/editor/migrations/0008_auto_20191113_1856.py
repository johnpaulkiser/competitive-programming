# Generated by Django 2.2.5 on 2019-11-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0007_auto_20191113_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubmission',
            name='language',
            field=models.CharField(choices=[('C', 'C'), ('JavaScript', 'JavaScript'), ('Java', 'Java'), ('Clojure', 'Clojure'), ('Python', 'Python'), ('C#', 'C#'), ('C++', 'C++')], default='Java', max_length=50),
        ),
    ]
