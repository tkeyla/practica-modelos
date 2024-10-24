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

# 4. Listar todas las épicas que tienen tareas en progreso.
def consulta4():
    epicas_en_progreso = Epica.objects.filter(tareas_asociadas__estado="EN_PROGRESO").distinct()
    return epicas_en_progreso

#6: 6. Obtener la suma de esfuerzo estimado de todas las tareas asociadas a una épica específica.

#7: Listar los sprints que tiene un Scrum Master asignado.
def consulta7(id):
    sprints = Sprint.objects.filter(scrum_master=id)
    return sprints

#CONSULTA 1
print("CONSULTA 1: \n")
tareas = consulta1(6)
for tarea in tareas:
    print(tarea)
    print("-" * 40) 

#CONSULTA 2
print("CONSULTA 2: \n")
tareas = consulta2(2)
for tarea in tareas:
    print(tarea)
    print("-" * 40) 

#CONSULTA 3
print("CONSULTA 3: \n")
tareas = consulta3(6)
for tarea in tareas:
    print(tarea)
    print("-" * 40)

#CONSULTA 4
print("CONSULTA 4: \n")
epicas = consulta4()
for epica in epicas:
    print(f"Épica: {epica.nombre}")
    print(f"Progreso: {epica.progreso}")
    print("-" * 40)

#CONSULTA 7
print("Consulta 7: \n")
sprints = consulta7(3)
for sprint in sprints:
    print (sprint)
    print("-" * 40)
