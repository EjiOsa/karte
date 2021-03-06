# Generated by Django 3.2.8 on 2021-10-08 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ja', models.CharField(max_length=128, unique=True, verbose_name='疾患名')),
                ('name_en', models.CharField(max_length=128, unique=True, verbose_name='疾患名(英語)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '疾患',
                'verbose_name_plural': '疾患',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='職種名')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '職種',
                'verbose_name_plural': '職種',
            },
        ),
        migrations.CreateModel(
            name='Rest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=32, unique=True, verbose_name='安静度')),
                ('area', models.CharField(max_length=128, verbose_name='活動範囲')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '安静度',
                'verbose_name_plural': '安静度',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='権限名')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('target', models.ForeignKey(max_length=32, on_delete=django.db.models.deletion.PROTECT, to='master.job', verbose_name='対象職種')),
            ],
            options={
                'verbose_name': '役職',
                'verbose_name_plural': '役職',
            },
        ),
    ]
