# Generated by Django 3.2.8 on 2021-10-08 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_alter_role_target'),
        ('staff', '0003_auto_20211008_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clerk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(default=None, max_length=64, verbose_name='苗字')),
                ('first_name', models.CharField(default=None, max_length=64, verbose_name='名前')),
                ('last_name_kana', models.CharField(default=None, max_length=64, verbose_name='みょうじ')),
                ('first_name_kana', models.CharField(default=None, max_length=64, verbose_name='なまえ')),
                ('age', models.PositiveSmallIntegerField(default=None, verbose_name='年齢')),
                ('sex', models.CharField(choices=[('male', '男性'), ('female', '女性')], max_length=8, verbose_name='性別')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.ForeignKey(limit_choices_to={'target': 'CLERK'}, on_delete=django.db.models.deletion.PROTECT, to='master.role', verbose_name='権限名')),
            ],
            options={
                'verbose_name': '事務員',
                'verbose_name_plural': '事務員',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(default=None, max_length=64, verbose_name='苗字')),
                ('first_name', models.CharField(default=None, max_length=64, verbose_name='名前')),
                ('last_name_kana', models.CharField(default=None, max_length=64, verbose_name='みょうじ')),
                ('first_name_kana', models.CharField(default=None, max_length=64, verbose_name='なまえ')),
                ('age', models.PositiveSmallIntegerField(default=None, verbose_name='年齢')),
                ('sex', models.CharField(choices=[('male', '男性'), ('female', '女性')], default=None, max_length=8, verbose_name='性別')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.ForeignKey(limit_choices_to={'target': 'DOCTOR'}, on_delete=django.db.models.deletion.PROTECT, to='master.role', verbose_name='権限名')),
            ],
            options={
                'verbose_name': '医師',
                'verbose_name_plural': '医師',
            },
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(default=None, max_length=64, verbose_name='苗字')),
                ('first_name', models.CharField(default=None, max_length=64, verbose_name='名前')),
                ('last_name_kana', models.CharField(default=None, max_length=64, verbose_name='みょうじ')),
                ('first_name_kana', models.CharField(default=None, max_length=64, verbose_name='なまえ')),
                ('age', models.PositiveSmallIntegerField(default=None, verbose_name='年齢')),
                ('sex', models.CharField(choices=[('male', '男性'), ('female', '女性')], default=None, max_length=8, verbose_name='性別')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.ForeignKey(limit_choices_to={'target': 'NURSE'}, on_delete=django.db.models.deletion.PROTECT, to='master.role', verbose_name='権限名')),
            ],
            options={
                'verbose_name': '看護師',
                'verbose_name_plural': '看護師',
            },
        ),
        migrations.CreateModel(
            name='Occupational',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(default=None, max_length=64, verbose_name='苗字')),
                ('first_name', models.CharField(default=None, max_length=64, verbose_name='名前')),
                ('last_name_kana', models.CharField(default=None, max_length=64, verbose_name='みょうじ')),
                ('first_name_kana', models.CharField(default=None, max_length=64, verbose_name='なまえ')),
                ('age', models.PositiveSmallIntegerField(default=None, verbose_name='年齢')),
                ('sex', models.CharField(choices=[('male', '男性'), ('female', '女性')], default=None, max_length=8, verbose_name='性別')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.ForeignKey(limit_choices_to={'target': 'OCCUPATIONAL'}, on_delete=django.db.models.deletion.PROTECT, to='master.role', verbose_name='権限名')),
            ],
            options={
                'verbose_name': '作業療法士',
                'verbose_name_plural': '作業療法士',
            },
        ),
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(default=None, max_length=64, verbose_name='苗字')),
                ('first_name', models.CharField(default=None, max_length=64, verbose_name='名前')),
                ('last_name_kana', models.CharField(default=None, max_length=64, verbose_name='みょうじ')),
                ('first_name_kana', models.CharField(default=None, max_length=64, verbose_name='なまえ')),
                ('age', models.PositiveSmallIntegerField(default=None, verbose_name='年齢')),
                ('sex', models.CharField(choices=[('male', '男性'), ('female', '女性')], default=None, max_length=8, verbose_name='性別')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.ForeignKey(limit_choices_to={'target': 'PHARMACIST'}, on_delete=django.db.models.deletion.PROTECT, to='master.role', verbose_name='権限名')),
            ],
            options={
                'verbose_name': '薬剤師',
                'verbose_name_plural': '薬剤師',
            },
        ),
        migrations.CreateModel(
            name='Physical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(default=None, max_length=64, verbose_name='苗字')),
                ('first_name', models.CharField(default=None, max_length=64, verbose_name='名前')),
                ('last_name_kana', models.CharField(default=None, max_length=64, verbose_name='みょうじ')),
                ('first_name_kana', models.CharField(default=None, max_length=64, verbose_name='なまえ')),
                ('age', models.PositiveSmallIntegerField(default=None, verbose_name='年齢')),
                ('sex', models.CharField(choices=[('male', '男性'), ('female', '女性')], default=None, max_length=8, verbose_name='性別')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.ForeignKey(limit_choices_to={'target': 'PHYSICAL'}, on_delete=django.db.models.deletion.PROTECT, to='master.role', verbose_name='権限名')),
            ],
            options={
                'verbose_name': '理学療法士',
                'verbose_name_plural': '理学療法士',
            },
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
