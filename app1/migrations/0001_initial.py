# Generated by Django 4.2.5 on 2023-10-20 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act1_usuario', models.CharField(max_length=150)),
                ('horas_diarias', models.IntegerField(default=0)),
                ('horas_descanso', models.IntegerField(default=0)),
                ('periodos_descando', models.IntegerField(default=0)),
                ('trabajo_sabado', models.CharField(max_length=5)),
                ('trabajo_domingo', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Activity3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act3_usuario', models.CharField(max_length=150)),
                ('turno', models.CharField(max_length=15)),
                ('turno_inicio', models.IntegerField(default=0)),
                ('turno_inicio_periodo', models.IntegerField(max_length=15)),
                ('turno_final', models.IntegerField(default=0)),
                ('turno_final_periodo', models.IntegerField(max_length=15)),
                ('turno_actividades', models.CharField(max_length=200)),
                ('turno_notas', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actN_usuario', models.CharField(max_length=150)),
                ('actividad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('state', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
            ],
        ),
    ]
