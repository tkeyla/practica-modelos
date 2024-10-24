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
from scrum_app.models import Sprint, Tarea, Epica

# 1. Crear usuarios (Scrum Masters, responsables y miembros del equipo)

usuarios = []

for i in range(10):
    usuario = User.objects.create_user(username=f'usuario{i}', password='password123')
    usuarios.append(usuario)

# 2. Crear Sprints
sprint1 = Sprint.objects.create(
    nombre="Sprint 1",
    objetivo="Objetivo del Sprint 1",
    fecha_inicio="2024-10-01",
    fecha_fin="2024-10-15",
    velocidad=40,
    scrum_master=usuarios[0],
)
sprint2 = Sprint.objects.create(
    nombre="Sprint 2",
    objetivo="Objetivo del Sprint 2",
    fecha_inicio="2024-10-16",
    fecha_fin="2024-10-30",
    velocidad=35,
    scrum_master=usuarios[1],
)
sprint3 = Sprint.objects.create(
    nombre="Sprint 3",
    objetivo="Objetivo del Sprint 3",
    fecha_inicio="2024-11-01",
    fecha_fin="2024-11-15",
    velocidad=50,
    scrum_master=usuarios[2],
)

# 3. Asignar miembros del equipo a los sprints
sprint1.equipo_desarrollo.add(usuarios[3], usuarios[4], usuarios[5])
sprint2.equipo_desarrollo.add(usuarios[6], usuarios[7], usuarios[8])
sprint3.equipo_desarrollo.add(usuarios[3], usuarios[7], usuarios[9])

# 4. Crear épicas
epica1 = Epica.objects.create(
    nombre="Epica 1",
    descripcion="Descripción de la épica 1",
    criterios_aceptacion="Criterios de aceptación de la épica 1",
    estado="POR_HACER",
    responsable=usuarios[0],
    esfuerzo_estimado_total=100,
    progreso=0.2
)

epica2 = Epica.objects.create(
    nombre="Epica 2",
    descripcion="Descripción de la épica 2",
    criterios_aceptacion="Criterios de aceptación de la épica 2",
    estado="EN_PROGRESO",
    responsable=usuarios[1],
    esfuerzo_estimado_total=80,
    progreso=0.5
)

# 5. Crear tareas y asignarlas a sprints y épicas
for i in range(1, 31):
    tarea = Tarea.objects.create(
        titulo=f"Tarea {i}",
        descripcion=f"Descripción de la tarea {i}",
        criterios_aceptacion=f"Criterios de aceptación de la tarea {i}",
        prioridad=i % 5,
        estado="POR_HACER" if i % 3 == 0 else "EN_PROGRESO" if i % 3 == 1 else "COMPLETADA",
        esfuerzo_estimado=i * 2,
        responsable=usuarios[i % 10],
        sprint_asignado=sprint1 if i <= 10 else sprint2 if i <= 20 else sprint3,
    )

    # Asignar tareas a épicas
    if i <= 15:
        epica1.tareas_asociadas.add(tarea)
    else:
        epica2.tareas_asociadas.add(tarea)

    # Asignar dependencias
    if i > 1:
        tarea.dependencias.add(Tarea.objects.get(titulo=f"Tarea {i-1}"))

# 6. Asignar backlog a los sprints
sprint1.backlog_sprint.add(*Tarea.objects.filter(sprint_asignado=sprint1))
sprint2.backlog_sprint.add(*Tarea.objects.filter(sprint_asignado=sprint2))
sprint3.backlog_sprint.add(*Tarea.objects.filter(sprint_asignado=sprint3))

print("Datos de prueba creados con éxito.")
