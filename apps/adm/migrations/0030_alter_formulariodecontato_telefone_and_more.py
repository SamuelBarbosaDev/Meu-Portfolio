# Generated by Django 4.1 on 2022-08-22 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0029_alter_formulariodecontato_telefone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulariodecontato',
            name='telefone',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='sobrehabilidade',
            name='porcentagem',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
