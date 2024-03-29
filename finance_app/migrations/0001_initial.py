# Generated by Django 4.1.3 on 2024-01-23 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryEarnings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Categoria dos ganhos',
                'verbose_name_plural': 'Categorias dos ganhos',
            },
        ),
        migrations.CreateModel(
            name='CategoryExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Categoria das despesas',
                'verbose_name_plural': 'Categorias das despesas',
            },
        ),
        migrations.CreateModel(
            name='UniqueID',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
                ('value', models.DecimalField(decimal_places=2, max_digits=50000000000000, verbose_name='Valor')),
                ('date', models.DateField(verbose_name='Data')),
                ('recurrence', models.BooleanField(default=False, verbose_name='Despesa recorrente')),
                ('type', models.CharField(default='expense', max_length=100, verbose_name='Tipo')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_app.categoryexpenses', verbose_name='Categoria')),
                ('unique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_app.uniqueid', verbose_name='ID único')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Despesa',
                'verbose_name_plural': 'Despesas',
            },
        ),
        migrations.CreateModel(
            name='Earnings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
                ('value', models.DecimalField(decimal_places=2, max_digits=50000000000000, verbose_name='Valor')),
                ('date', models.DateField(verbose_name='Data')),
                ('recurrence', models.BooleanField(default=False, verbose_name='Recorrência')),
                ('type', models.CharField(default='earning', max_length=15, verbose_name='Tipo')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_app.categoryearnings', verbose_name='Categoria')),
                ('unique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_app.uniqueid', verbose_name='ID único')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Ganho',
                'verbose_name_plural': 'Ganhos',
            },
        ),
    ]
