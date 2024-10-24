#NOTA: EJECUTAR DESDE EL SHELL (ESTE SCRIPT ES SOLO DE PRUEBA, NO ES DEL PUNTO 4)

from django.contrib.auth.models import User
from scrum_app.models import Sprint, Tarea, Epica

print(f"Tareas: {Tarea.objects.count()}")  
print(f"Epicas: {Epica.objects.count()}")  
print(f"Sprints: {Sprint.objects.count()}") 
print(f'Usuarios: {User.objects.count()}')  
