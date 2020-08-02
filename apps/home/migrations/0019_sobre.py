# Generated by Django 3.0.8 on 2020-07-20 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20200719_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo1', models.CharField(default='', max_length=20)),
                ('titulo2', models.CharField(default='', max_length=30)),
                ('descricao', models.TextField(blank=True, default='', null=True)),
                ('imagem1', models.ImageField(blank=True, null=True, upload_to='home_sobre')),
                ('seo_imagem1', models.CharField(blank=True, default='', max_length=45, null=True)),
                ('imagem2', models.ImageField(blank=True, null=True, upload_to='home_sobre')),
                ('seo_imagem2', models.CharField(blank=True, default='', max_length=45, null=True)),
                ('imagem3', models.ImageField(blank=True, null=True, upload_to='home_sobre')),
                ('seo_imagem3', models.CharField(blank=True, default='', max_length=45, null=True)),
                ('imagem4', models.ImageField(blank=True, null=True, upload_to='home_sobre')),
                ('seo_imagem4', models.CharField(blank=True, default='', max_length=45, null=True)),
            ],
        ),
    ]
