from django.db.models import Sum, Count, Q
from scrum_app.models import Tarea, Sprint, Epica, User

#1: Obtener todas las tareas asignadas a un usuario específico.
def consulta1(responsable_id):
    tareas = Tarea.objects.filter(responsable = responsable_id)
    return tareas

#2: Obtener las tareas completadas dentro de un sprint determinado.
def consulta2(sprint_id):
    sprint = Sprint.objects.get(id=sprint_id)
    return Tarea.objects.filter(sprint_asignado=sprint, estado="COMPLETADA")

#3: Listar todas las tareas que dependen de una tarea específica.
def consulta3(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    return tarea.dependencias.all()

#CONSULTA 1
print("CONSULTA 1: \n")
tareas = consulta1(6)
for tarea in tareas:
    print(f"Título: {tarea.titulo}")
    print(f"Descripción: {tarea.descripcion}")
    print(f"Estado: {tarea.estado}")
    print(f"Responsable: {tarea.responsable.username}")
    print("-" * 40) 

#CONSULTA 2
print("CONSULTA 2: \n")
tareas = consulta2(2)
for tarea in tareas:
    print(f"Título: {tarea.titulo}")
    print(f"Descripción: {tarea.descripcion}")
    print(f"Estado: {tarea.estado}")
    print(f"Responsable: {tarea.responsable.username}")
    print(f"Sprint asignado: {tarea.sprint_asignado.nombre}")
    print("-" * 40) 

#CONSULTA 3
print("CONSULTA 3: \n")
tareas = consulta3(6)
for tarea in tareas:
    print(f"Título: {tarea.titulo}")
    print(f"Descripción: {tarea.descripcion}")
    print(f"Estado: {tarea.estado}")
    print(f"Responsable: {tarea.responsable.username}")
    print(f"Sprint asignado: {tarea.sprint_asignado.nombre}")
    print("-" * 40) 