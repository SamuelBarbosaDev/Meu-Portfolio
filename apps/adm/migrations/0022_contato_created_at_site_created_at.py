# Generated by Django 4.1 on 2022-08-19 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0021_sobre_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
