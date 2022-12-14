# Generated by Django 4.1 on 2022-08-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0006_remove_sobre_perfil_imagem_sobre_foto_de_perfil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='footer',
            field=models.FileField(blank=True, default='site/images/footer.webp', null=True, upload_to='site/images/'),
        ),
        migrations.AlterField(
            model_name='sobre',
            name='background_depoimento',
            field=models.FileField(blank=True, default='sobre/images/backgroud.jpg', null=True, upload_to='sobre/images/'),
        ),
        migrations.AlterField(
            model_name='sobre',
            name='foto_de_perfil',
            field=models.FileField(blank=True, default='sobre/images/foto_de_perfil.svg', null=True, upload_to='sobre/images/'),
        ),
        migrations.AlterField(
            model_name='sobre',
            name='hero',
            field=models.FileField(blank=True, default='sobre/images/hero.webp', null=True, upload_to='sobre/images/'),
        ),
    ]
