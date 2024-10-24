# Proyecto Scrum - Scripts de Gestión de Datos

Este repositorio contiene varios scripts para la gestión y manipulación de datos relacionados con un proyecto Scrum en una aplicación Django. A continuación, se detalla el uso de cada archivo Python proporcionado.

# Requisitos previos
Antes de comenzar, asegúrate de tener instalados los siguientes programas:

-Python
-Django: El proyecto está desarrollado en Django, por lo que debes tenerlo instalado.
-PostgreSQL: El servidor de base de datos utilizado es PostgreSQL, por lo que deberás tenerlo instalado y un usuario postgres y base de datos postgres con contraseña 12345 o modificarlo en settings.py
-Git: Para clonar el repositorio remoto, asegúrate de tener Git instalado.

## Instrucciones de instalación

### 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local. Abre una terminal y ejecuta el siguiente comando:
git clone <URL_DEL_REPOSITORIO>

### 2. Crear y activar un entorno virtual
cd <nombre_del_directorio_clonado>
python -m venv env

Para activar el entorno virtual:
En Windows: env\Scripts\activate
En Linux/macOS: source env/bin/activate

### 3. Instalar las dependencias
Con el entorno virtual activado, instala las dependencias del proyecto ejecutando el siguiente comando: pip install -r requirements.txt

### 4. Intala y configra PostgreSQL

### 5. Migraciones de base de datos
python manage.py migrate

### 6. Ejecutar el servidor
python manage.py runserver
El servidor estará disponible en http://localhost:8000.

## Scripts

### 1. `limpiarDatos.py`
Este script elimina datos de la base de datos relacionados con tareas, épicas, sprints y usuarios específicos. Está diseñado para realizar una limpieza completa de los datos en el entorno de desarrollo.

#### Funcionalidades:
- Elimina todas las **tareas**, **épicas** y **sprints** de la base de datos.
- Elimina usuarios cuyos nombres comiencen con "scrumMaster", "responsable" y "miembroEquipo".
- Imprime la cantidad restante de tareas, épicas, sprints y usuarios luego de la eliminación.
- Resetea las secuencias de IDs para asegurarse de que los próximos registros comiencen con los valores correctos.

**Advertencia**: Este script debe ser ejecutado con **responsabilidad**, ya que elimina de forma irreversible todos los datos mencionados.

#### Uso:
```
python manage.py shell <
scrum_app/limpiarDatos.py
```

### 2. `models.py`
Contiene los modelos de la aplicación **Scrum** en Django, que representan las siguientes entidades:

- **Sprint**: Período de tiempo durante el cual el equipo trabaja en completar tareas.
- **Tarea**: Unidad de trabajo asignada a miembros del equipo dentro de un sprint.
- **Épica**: Grupo grande de trabajo que se desglosa en varias tareas.

Los modelos incluyen restricciones en las fechas y esfuerzos estimados.

### 3. `scriptsConsulta.py`
Este archivo contiene consultas comunes a la base de datos relacionadas con las tareas, épicas y sprints en el contexto Scrum.

#### Funcionalidades:
- Obtener todas las tareas asignadas a un usuario específico.
- Listar las tareas completadas dentro de un sprint.
- Obtener tareas que dependen de una tarea específica.
- Listar épicas con tareas en progreso.
- Obtener la suma del esfuerzo estimado de las tareas asociadas a una épica.
- Listar sprints con un Scrum Master asignado.

#### Uso:
Las consultas pueden ejecutarse dentro del shell de Django de la siguiente manera:
```
python manage.py shell<
scrum_app/scriptConsultas.py
```

### 4. `scriptPoblacion.py`
Este script genera datos iniciales para poblar la base de datos con **usuarios**, **sprints**, **épicas** y asignaciones de equipo de desarrollo.

#### Funcionalidades:
- Crear usuarios para Scrum Masters, responsables y miembros del equipo.
- Crear y poblar sprints con los datos generados.
- Asignar miembros del equipo a los sprints.
- Crear épicas y asociarlas a responsables y tareas.

#### Uso:
Este script está diseñado para ser ejecutado una sola vez para poblar la base de datos:
```
python manage.py shell<
scrum_app/scriptPoblacion.py
```

**Nota**: En caso de errores o si desea resetear los datos, puede usar `limpiarDatos.py` antes de ejecutar nuevamente este script.

Recuerde ejecutar estos scripts en un entorno controlado, especialmente aquellos que eliminan datos o realizan operaciones críticas.
