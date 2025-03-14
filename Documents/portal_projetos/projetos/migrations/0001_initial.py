# Generated by Django 5.1.6 on 2025-03-14 20:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('cliente', models.CharField(max_length=200)),
                ('data_inicio', models.DateField()),
                ('data_prevista_conclusao', models.DateField()),
                ('data_real_conclusao', models.DateField(blank=True, null=True)),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=300)),
                ('data_inicio', models.DateField()),
                ('data_prevista_conclusao', models.DateField()),
                ('data_real_conclusao', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Em andamento', 'Em andamento'), ('Atrasado', 'Atrasado'), ('Bloqueado', 'Bloqueado'), ('Concluído', 'Concluído')], default='Pendente', max_length=20)),
                ('motivo_status', models.TextField(blank=True, null=True)),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atividades', to='projetos.projeto')),
            ],
        ),
    ]
