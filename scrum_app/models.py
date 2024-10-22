from django.db import models
from django.contrib.auth.models import User

class Sprint(models.Model):
    nombre = models.CharField(max_length=200)
    objetivo = models.TextField(blank=True, default='')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    velocidad = models.IntegerField()
    scrum_master = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    equipo_desarrollo = models.ManyToManyField(User, related_name='sprints', blank=True)
    backlog_sprint = models.ManyToManyField('Tarea', related_name='sprints', blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(fecha_fin__gte=models.F('fecha_inicio')), name='fecha_fin_posterior'),
            models.CheckConstraint(check=models.Q(velocidad__gte=0), name='velocidad_no_negativa'),
        ] 

class Tarea(models.Model):
    
    ESTADO_CHOICES = [
        ("POR_HACER", 'Por hacer'),
        ("EN_PROGRESO", 'En progreso'),
        ("COMPLETADA", 'Completada'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, default='')
    criterios_aceptacion = models.TextField(blank=True, default='')
    prioridad = models.IntegerField()
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default="POR_HACER")
    esfuerzo_estimado = models.IntegerField()
    responsable = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    sprint_asignado = models.ForeignKey(Sprint, null=True, on_delete=models.SET_NULL)
    dependencias = models.ManyToManyField('self', symmetrical=False, blank=True)
    bloqueadores = models.TextField(blank=True, default='')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(prioridad__gte=0), name='prioridad_no_negativa'),
            models.CheckConstraint(check=models.Q(esfuerzo_estimado__gte=0), name='esfuerzo_estimado_no_negativo'),
            models.CheckConstraint(check=models.Q(estado__in=["POR_HACER", "EN_PROGRESO", "COMPLETADA"]), name='estado_valido_tarea'),
            models.UniqueConstraint(fields=['titulo','sprint_asignado'], name='unique_tarea_sprint'),
        ] 

class Epica(models.Model):

    ESTADO_CHOICES = [
        ("POR_HACER", 'Por hacer'),
        ("EN_PROGRESO", 'En progreso'),
        ("COMPLETADA", 'Completada'),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, default='')
    criterios_aceptacion = models.TextField(blank=True, default='')
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default="POR_HACER")
    responsable = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    tareas_asociadas = models.ManyToManyField(Tarea, related_name='epicas')
    esfuerzo_estimado_total = models.IntegerField()
    progreso = models.FloatField()
    dependencias = models.ManyToManyField('self', symmetrical=False, blank=True)
    fecha_inicio = models.DateTimeField(blank=True, default='')
    fecha_fin = models.DateTimeField(blank=True, default='')

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(esfuerzo_estimado_total__gte=0), name='esfuerzo_total_no_negativo'),
            models.CheckConstraint(check=models.Q(progreso__gte=0) & models.Q(progreso__lte=1), name='progreso_valido'),
            models.CheckConstraint(check=models.Q(estado__in=["POR_HACER", "EN_PROGRESO", "COMPLETADA"]), name='estado_valido_epica'),
            models.CheckConstraint(check=models.Q(fecha_fin__gte=models.F('fecha_inicio')), name='fecha_fin_posterior_epica')
        ]