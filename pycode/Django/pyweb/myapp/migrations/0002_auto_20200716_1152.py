# Generated by Django 3.0.3 on 2020-07-16 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.CharField(max_length=100, verbose_name='mid')),
                ('name', models.CharField(max_length=800, verbose_name='name')),
                ('sign', models.CharField(blank=True, max_length=800, null=True, verbose_name='sign')),
                ('level', models.CharField(max_length=10, verbose_name='level')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
