# Generated by Django 4.1 on 2022-08-22 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0028_alter_portfólio_imagem_do_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulariodecontato',
            name='telefone',
            field=models.IntegerField(max_length=11),
        ),
        migrations.AlterField(
            model_name='sobrehabilidade',
            name='porcentagem',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]