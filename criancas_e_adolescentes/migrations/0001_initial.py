# Generated by Django 4.2.6 on 2023-10-15 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crianca_e_Adolescente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=194, verbose_name='Nome completo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('numero_casa', models.PositiveSmallIntegerField(verbose_name='Número da casa a ser visitada')),
                ('placa_veiculo', models.CharField(blank=True, max_length=7, null=True, verbose_name='Placa do veículo')),
                ('horario_chegada', models.DateTimeField(auto_now_add=True, verbose_name='Horário de chegada na portaria')),
                ('horario_saida', models.DateTimeField(blank=True, null=True, verbose_name='Horário de saída do condomínio')),
                ('horario_autorizacao', models.DateTimeField(blank=True, null=True, verbose_name='Horário de autorização de entrada')),
                ('morador_responsavel', models.CharField(blank=True, max_length=194, verbose_name='Nome do morador responsável por autorizar a entrada do visitante')),
                ('registrado_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adms.adm', verbose_name='ADM responsável pelo registro')),
            ],
            options={
                'verbose_name': 'Crianca_e_Adolescente',
                'verbose_name_plural': 'Criancas_e_Adolescestes',
                'db_table': 'crianca_e_adolescente',
            },
        ),
    ]
