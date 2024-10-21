"""

El set de datos debe incluir:
1. Al menos 10 usuarios (responsables, Scrum Masters y miembros del
equipo).
2. Al menos 30 tareas, distribuidas en diferentes sprints y épicas.
3. Al menos 3 sprints con equipos de desarrollo y backlog asignado.
4. Varias dependencias entre tareas y épicas

NOTA: Esto esta sujeto a cambios y mejoras, use algoritmos que capaz no hayamos visto aunque
son simples y cumplen la funcion.

"""

from django.contrib.auth.models import User
from datetime import date, timedelta
from random import randint, choice
from .models import Sprint, Tarea, Epica  

#Creacion de usuarios
for i in range(1, 11):
    User.objects.create_user(username=f'user{i}', password='password123')

#Asignar usuarios aleatoriamente para Scrum Masters y equipo de desarrollo
usuarios = list(User.objects.all())

#Creacion de los sprint
sprint1 = Sprint.objects.create(
    nombre='Sprint 1', 
    objetivo='Objetivo del Sprint 1',
    fecha_inicio=date.today(), 
    fecha_fin=date.today() + timedelta(days=14), 
    velocidad=randint(20, 40),
    scrum_master=choice(usuarios)
)
sprint2 = Sprint.objects.create(
    nombre='Sprint 2', 
    objetivo='Objetivo del Sprint 2',
    fecha_inicio=date.today() + timedelta(days=15), 
    fecha_fin=date.today() + timedelta(days=29), 
    velocidad=randint(20, 40),
    scrum_master=choice(usuarios)
)
sprint3 = Sprint.objects.create(
    nombre='Sprint 3', 
    objetivo='Objetivo del Sprint 3',
    fecha_inicio=date.today() + timedelta(days=30), 
    fecha_fin=date.today() + timedelta(days=44), 
    velocidad=randint(20, 40),
    scrum_master=choice(usuarios)
)

#Se asigna un equipo de desarrollo a cada sprint
for sprint in [sprint1, sprint2, sprint3]:
    equipo = [choice(usuarios) for _ in range(5)]  #5 usuarios por sprint
    sprint.equipo_desarrollo.add(*equipo)

#Se crean las epicas
epica1 = Epica.objects.create(
    nombre='Épica 1',
    descripcion='Descripción de la épica 1',
    estado='POR_HACER',
    responsable=choice(usuarios),
    esfuerzo_estimado_total=100,
    progreso=0
)
epica2 = Epica.objects.create(
    nombre='Épica 2',
    descripcion='Descripción de la épica 2',
    estado='EN_PROGRESO',
    responsable=choice(usuarios),
    esfuerzo_estimado_total=80,
    progreso=0.5
)

#Se crean tareas y se las asignan a sprints o epicas
for i in range(1, 31):
    tarea = Tarea.objects.create(
        titulo=f'Tarea {i}',
        descripcion=f'Descripción de la tarea {i}',
        prioridad=randint(1, 10),
        estado=choice(['POR_HACER', 'EN_PROGRESO', 'COMPLETADA']),
        esfuerzo_estimado=randint(1, 20),
        responsable=choice(usuarios),
        sprint_asignado=choice([sprint1, sprint2, sprint3])
    )

    #Se asignan algunas tareas a épicas
    if i % 2 == 0:
        epica1.tareas_asociadas.add(tarea)
    else:
        epica2.tareas_asociadas.add(tarea)

    #Se agregan dependencias aleatorias entre tareas
    if i > 5:  #Se agregan dependencias a partir de la tarea 6
        dependencias = Tarea.objects.filter(id__lt=tarea.id).order_by('?')[:randint(1, 3)]
        tarea.dependencias.add(*dependencias)

#Se asignan tareas a cada sprint
sprint1.backlog_sprint.add(*Tarea.objects.filter(sprint_asignado=sprint1))
sprint2.backlog_sprint.add(*Tarea.objects.filter(sprint_asignado=sprint2))
sprint3.backlog_sprint.add(*Tarea.objects.filter(sprint_asignado=sprint3))

#Se crean dependencias entre épicas
epica1.dependencias.add(epica2)

print("Datos poblados correctamente.")
