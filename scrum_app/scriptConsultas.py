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

#4: Listar todas las épicas que tienen tareas en progreso.
def consulta4():
    return Epica.objects.filter(tareas_asociadas__estado="EN_PROGRESO").distinct()

#5: Calcular el número total de tareas por estado (por hacer, en progreso, completada).
def consulta5():
    return Tarea.objects.values('estado').annotate(total=Count('estado'))

#6: 6. Obtener la suma de esfuerzo estimado de todas las tareas asociadas a una épica específica.
def consulta6(epica_id):
    epica = Epica.objects.get(id=epica_id)
    return epica.tareas_asociadas.aggregate(total_esfuerzo=Sum('esfuerzo_estimado'))

#7: Listar los sprints que tiene un Scrum Master asignado.
def consulta7(id):
    sprints = Sprint.objects.filter(scrum_master=id)
    return sprints

#8: Obtener el progreso total de una épica en base a las tareas completadas.
def consulta8(epica_id):
    epica = Epica.objects.get(id=epica_id)
    total_tareas = epica.tareas_asociadas.count()
    
    if total_tareas == 0:
        return 0.0 

    tareas_completadas = epica.tareas_asociadas.filter(estado="COMPLETADA").count()
    progreso = tareas_completadas / total_tareas
    return round(progreso, 2) 

#9: Obtener el backlog de un sprint específico y sus responsables.
def consulta9(sprint_id):
    sprint = Sprint.objects.get(id=sprint_id)
    return sprint.backlog_sprint.values('titulo', 'responsable__username')

#10: Listar todas las tareas que están bloqueadas.
def consulta10():
    return Tarea.objects.filter(~Q(bloqueadores=''))

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

#CONSULTA 5
print("CONSULTA 5: \n")
tareas = consulta5()
for tarea in tareas:
    print(tarea)
    print("-" * 40)

#CONSULTA 6
print("CONSULTA 6: \n")
resultado = consulta6(2)
print(resultado)
print("-" * 40)

#CONSULTA 7
print("Consulta 7: \n")
sprints = consulta7(3)
for sprint in sprints:
    print (sprint)
    print("-" * 40)

#CONSULTA 8
print("Consulta 8: \n")
resultado = consulta8(2)
print (resultado)
print("-" * 40)

#CONSULTA 9
print("Consulta 9: \n")
sprints = consulta9(2)
for sprint in sprints:
    print (sprint)
    print("-" * 40)

#CONSULTA 10
print("Consulta 10: \n")
tareas = consulta10()
for tarea in tareas:
    print (tarea)
    print("-" * 40)