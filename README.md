# Proyecto Scrum - Scripts de Gestión de Datos

Este repositorio contiene varios scripts para la gestión y manipulación de datos relacionados con un proyecto Scrum en una aplicación Django. A continuación, se detalla el uso de cada archivo Python proporcionado.

# Requisitos previos
Antes de comenzar, asegúrate de tener instalados las siguientes herramientas:

-Python: En su version 3.10
-Git: Para clonar el repositorio remoto, asegúrate de tener Git instalado.

## Instrucciones de instalación

### 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local. En una ubicación deseada, abre una terminal y ejecuta el siguiente comando:

`git clone <URL_DEL_REPOSITORIO>`

Se va a crear una carpeta practica-modelos dentro, que contendra el proyecto.

### 2. Crear y activar un entorno virtual

En una carpeta aparte del proyecto, ejecutar este comando:

`python -m venv env`

Para activar el entorno virtual:

En Windows: `env\Scripts\activate`
En Linux/macOS: `source env/bin/activate`

### 3. Instalar las dependencias

Moverse con el entorno virtual activado a la carpeta practica-modelos descargada del repositorio remoto, e instalar las dependencias del proyecto en el entorno virtual ejecutando el siguiente comando: 

`pip install -r requirements.txt`

### 4. Migraciones de base de datos

Ejecutar inmediatamente este comando para ejecutar la migración inicial:

`python manage.py migrate`

## Descripción del modelo

Contiene los modelos de la aplicación **Scrum** en Django, que representan las siguientes entidades:

- **Sprint**: Período de tiempo durante el cual el equipo trabaja en completar tareas.
- **Tarea**: Unidad de trabajo asignada a miembros del equipo dentro de un sprint.
- **Épica**: Grupo grande de trabajo que se desglosa en varias tareas.

Los modelos incluyen restricciones en las fechas y esfuerzos estimados.

## Scripts

Para ejecutar los scripts y empezar a usar la aplicación, estar con el entorno virtual activo
en una consola en la carpeta practica-modelos y ejecutar los comandos mostrados abajo en orden.

### 1. `scriptPoblacion.py`
Este script genera datos iniciales para poblar la base de datos con **usuarios**, **sprints**, **épicas** y asignaciones de equipo de desarrollo.

#### Funcionalidades:
- Crear usuarios para Scrum Masters, responsables y miembros del equipo.
- Crear y poblar sprints con los datos generados.
- Asignar miembros del equipo a los sprints.
- Crear épicas y asociarlas a responsables y tareas.

#### Uso:

Este script está diseñado para ser ejecutado una sola vez para poblar la base de datos:

`python manage.py shell < scrum_app/scriptPoblacion.py`

### 2. `scriptsConsulta.py`

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

`python manage.py shell < scrum_app/scriptConsultas.py`

### 3. `limpiarDatos.py (OPCIONAL)`
Este script elimina datos de la base de datos relacionados con tareas, épicas, sprints y usuarios específicos. Está diseñado para realizar una limpieza completa de los datos en el entorno de desarrollo.

#### Funcionalidades:
- Elimina todas las **tareas**, **épicas**, **sprints** y las tablas creadas por ManyToManyField, de la base de datos.
- Elimina usuarios cuyos nombres comiencen con "scrumMaster", "responsable" y "miembroEquipo".
- Imprime la cantidad restante de tareas, épicas, sprints y usuarios luego de la eliminación.
- Resetea las secuencias de IDs para asegurarse de que los próximos registros comiencen con los valores correctos.

**Advertencia**: Este script debe ser ejecutado con **responsabilidad**, ya que elimina de forma irreversible todos los datos mencionados.

#### Uso:

`python manage.py shell < scrum_app/limpiarDatos.py`

**Nota**: En caso de errores o si desea resetear los datos, puede usar `limpiarDatos.py` antes de ejecutar nuevamente este script.
