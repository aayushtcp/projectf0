# Generated by Django 4.1.7 on 2023-06-06 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_allperson_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allperson',
            name='slug',
            field=models.CharField(default='this-s', max_length=130),
        ),
    ]