from django.db import models

class Activity1 (models.Model):
    act1_usuario = models.CharField(max_length = 150)
    horas_diarias = models.IntegerField(default=0)
    horas_descanso = models.IntegerField(default=0)
    periodos_descando = models.IntegerField(default=0)
    trabajo_sabado = models.CharField(max_length=5)
    trabajo_domingo = models.CharField(max_length=5)

class Activity3 (models.Model):
    act3_usuario = models.CharField(max_length = 150)
    turno = models.CharField(max_length = 15)
    turno_inicio = models.IntegerField(default=0)
    turno_inicio_periodo = models.IntegerField(max_length = 15)
    turno_final = models.IntegerField(default=0)
    turno_final_periodo = models.IntegerField(max_length = 15)
    turno_actividades = models.CharField(max_length=200)
    turno_notas = models.CharField(max_length=200)
    
class ActivityN (models.Model):
    actN_usuario = models.CharField(max_length = 150)
    actividad = models.CharField(max_length = 20)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    state = models.IntegerField(default = 0)

    
class State(models.Model):
    question_text = models.CharField(max_length=200)

    

    