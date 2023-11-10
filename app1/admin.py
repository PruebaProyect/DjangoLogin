from django.contrib import admin
from .models import Activity1, Activity3, ActivityN, Question, State




class Activity1Admin(admin.ModelAdmin):
    list_display = ('act1_usuario', 'horas_diarias', 'horas_descanso', 'periodos_descando', 'trabajo_sabado', 'trabajo_domingo')
    
class ActivityNAdmin(admin.ModelAdmin):
    list_display = ('actN_usuario', 'actividad')
    
class Activity3Admin(admin.ModelAdmin):
    list_display = ('act3_usuario', 'turno', 'turno_inicio', 'turno_inicio_periodo', 'turno_final', 'turno_final_periodo','turno_actividades','turno_notas')
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'state')
   
admin.site.register(Activity1, Activity1Admin)
admin.site.register(ActivityN, ActivityNAdmin)
admin.site.register(Activity3)
admin.site.register(Question, QuestionAdmin)