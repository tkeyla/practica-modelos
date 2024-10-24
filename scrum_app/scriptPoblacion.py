#NOTA: EJECUTAR UNA UNICA VEZ!!! EN CASO DE ERROR USAR EL SCRIPT DE limpiarDatos.py

from django.contrib.auth.models import User
from scrum_app.models import Sprint, Tarea, Epica

#1: Crear usuarios (Scrum Masters, responsables y miembros del equipo)
scrumMasters = []
responsables = []
miembrosEquipo = []

# Scrum Masters
for i in range(3):
    scrumMaster = User.objects.create_user(username=f'scrumMaster{i}', password='password123')
    scrumMasters.append(scrumMaster)

# Responsables
for i in range(6):
    responsable = User.objects.create_user(username=f'responsable{i}', password='password123')
    responsables.append(responsable)

# Miembros de equipo
for i in range(9):
    miembroEquipo = User.objects.create_user(username=f'miembroEquipo{i}', password='password123')
    miembrosEquipo.append(miembroEquipo)

#2: Crear Sprints
sprint1 = Sprint.objects.create(
    nombre="Sprint 1",
    objetivo="Objetivo del Sprint 1",
    fecha_inicio="2024-10-01",
    fecha_fin="2024-10-15",
    velocidad=40,
    scrum_master=scrumMasters[0],
)
sprint2 = Sprint.objects.create(
    nombre="Sprint 2",
    objetivo="Objetivo del Sprint 2",
    fecha_inicio="2024-10-16",
    fecha_fin="2024-10-30",
    velocidad=35,
    scrum_master=scrumMasters[1],
)
sprint3 = Sprint.objects.create(
    nombre="Sprint 3",
    objetivo="Objetivo del Sprint 3",
    fecha_inicio="2024-11-01",
    fecha_fin="2024-11-15",
    velocidad=50,
    scrum_master=scrumMasters[2],
)

#3: Asignar miembros del equipo a los sprints
sprint1.equipo_desarrollo.add(miembrosEquipo[0], miembrosEquipo[1], miembrosEquipo[2])
sprint2.equipo_desarrollo.add(miembrosEquipo[3], miembrosEquipo[4], miembrosEquipo[5])
sprint3.equipo_desarrollo.add(miembrosEquipo[6], miembrosEquipo[7], miembrosEquipo[8])

#4: Crear épicas
epica1 = Epica.objects.create(
    nombre="Epica 1",
    descripcion="Descripción de la épica 1",
    criterios_aceptacion="Criterios de aceptación de la épica 1",
    estado="POR_HACER",
    responsable=responsables[0],  # Corregido
    esfuerzo_estimado_total=100,
    progreso=0.2
)

epica2 = Epica.objects.create(
    nombre="Epica 2",
    descripcion="Descripción de la épica 2",
    criterios_aceptacion="Criterios de aceptación de la épica 2",
    estado="EN_PROGRESO",
    responsable=responsables[1],  # Corregido
    esfuerzo_estimado_total=80,
    progreso=0.5
)

#5: Crear tareas y asignarlas a sprints y épicas
for i in range(1, 31):
    tarea = Tarea.objects.create(
        titulo=f"Tarea {i}",
        descripcion=f"Descripción de la tarea {i}",
        criterios_aceptacion=f"Criterios de aceptación de la tarea {i}",
        prioridad=i % 5,
        estado="POR_HACER" if i % 3 == 0 else "EN_PROGRESO" if i % 3 == 1 else "COMPLETADA",
        esfuerzo_estimado=i * 2,
        responsable=responsables[i % 6],  # Corregido el subscript de responsables
        sprint_asignado=sprint1 if i <= 10 else sprint2 if i <= 20 else sprint3,
    )

    #Asignar tareas a épicas
    if i <= 15:
        epica1.tareas_asociadas.add(tarea)
    else:
        epica2.tareas_asociadas.add(tarea)

    #Asignar dependencias
    if i > 1:
        tarea.dependencias.add(Tarea.objects.get(titulo=f"Tarea {i-1}"))

#6: Asignar backlog a los sprints
sprint1.backlog_sprint.add(*Tarea.objects.filter(sprint_asignado=sprint1))
sprint2.backlog_sprint.add(*Tarea.objects.filter(sprint_asignado=sprint2))
sprint3.backlog_sprint.add(*Tarea.objects.filter(sprint_asignado=sprint3))

print("Datos de prueba creados correctamente!.")
