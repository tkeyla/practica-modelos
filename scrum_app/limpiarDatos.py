#NOTA: EJECUTAR DESDE EL SHELL CON RESPONSABILIDAD!!!

from django.contrib.auth.models import User
from scrum_app.models import Sprint, Tarea, Epica
from django.db import connection

#Eliminar todas las tareas
Tarea.objects.all().delete()

#Eliminar todas las épicas
Epica.objects.all().delete()

#Eliminar todos los sprints
Sprint.objects.all().delete()

#Eliminar usuarios específicos
User.objects.filter(username__startswith="scrumMaster").delete()
User.objects.filter(username__startswith="responsable").delete()
User.objects.filter(username__startswith="miembroEquipo").delete()

#Verificar que los datos se han eliminado
print(f"Tareas restantes: {Tarea.objects.count()}")
print(f"Épicas restantes: {Epica.objects.count()}")
print(f"Sprints restantes: {Sprint.objects.count()}")
print(f"Usuarios scrumMaster restantes: {User.objects.filter(username__startswith='scrumMaster').count()}")

# Resetear las secuencias de IDs
with connection.cursor() as cursor:
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='auth_user';")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='scrum_app_epica';")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='scrum_app_epica_dependencias';")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='scrum_app_epica_tareas_asociadas';")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='scrum_app_sprint';")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='scrum_app_sprint_backlog_sprint';")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='scrum_app_sprint_equipo_desarrollo';")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='scrum_app_tarea';")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='scrum_app_tarea_dependencias';")

print("Se resetearon los ID correctamente!")
