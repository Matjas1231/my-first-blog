# Generated by Django 2.2.12 on 2020-05-20 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200520_2109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text_text',
            new_name='text',
        ),
    ]
