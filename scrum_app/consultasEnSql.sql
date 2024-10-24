--NOTA: SOLO EJECUTAR ESTO DESDE DBEAVER; BORRAR DESPUES Y UNA VEZ SE TENGAN LAS CONSULTAS DESDE PYTHON SHELL

/*Consultas y Agregaciones:
○ Ejecuta al menos 10 consultas en el shell de Django o mediante vistas que
demuestren el funcionamiento de tu sistema. Utiliza los conceptos de
Consultas y Agregaciones para extraer información relevante.
○ Las consultas deben incluir:
1. Obtener todas las tareas asignadas a un usuario específico.
2. Obtener las tareas completadas dentro de un sprint determinado.
3. Listar todas las tareas que dependen de una tarea específica.
4. Listar todas las épicas que tienen tareas en progreso.
5. Calcular el número total de tareas por estado (por hacer, en progreso,
completada).
6. Obtener la suma de esfuerzo estimado de todas las tareas asociadas
a una épica específica.
7. Listar los sprints que tiene un Scrum Master asignado.
8. Obtener el progreso total de una épica en base a las tareas
completadas.
9. Obtener el backlog de un sprint específico y sus responsables.
10. Listar todas las tareas que están bloqueadas.
*/

select * from scrum_app_tarea sat
join auth_user au ON sat.responsable_id = au.id 
where au.username = 'responsable2'

select * from scrum_app_tarea sat 
join scrum_app_sprint_backlog_sprint sasbs on sat.id = sasbs.tarea_id
join scrum_app_sprint sas on sasbs.sprint_id = sas.id 
where sat.estado = 'COMPLETADA' and sas.nombre = 'Sprint 2'

--EN REVISION
select * from scrum_app_tarea sat 
join scrum_app_tarea_dependencias satd on sat.id = satd.from_tarea_id 
join scrum_app_tarea_dependencias satd2 on sat.id = satd2.to_tarea_id 
where sat.titulo = 'Tarea 10'

select * from scrum_app_epica sae 
join scrum_app_epica_tareas_asociadas saeta on sae.id = saeta.epica_id
join scrum_app_tarea sat on saeta.tarea_id = sat.id 
where sat.estado = 'EN_PROGRESO'

select sat.estado, COUNT(*) from scrum_app_tarea sat  
group by sat.estado 

select sum(sat.esfuerzo_estimado) as Esfuerzo from scrum_app_tarea sat 
join scrum_app_epica_tareas_asociadas saeta on sat.id = saeta.tarea_id 
join scrum_app_epica sae ON saeta.epica_id = sae.id 
where sae.nombre = 'Epica 2'

select * FROM scrum_app_sprint sas
where scrum_master_id is NOT NULL 

-- EN REVISION
select * from scrum_app_epica sae

select sasbs.*, au.username from scrum_app_sprint_backlog_sprint sasbs 
join scrum_app_sprint sas ON sasbs.sprint_id = sas.id 
join scrum_app_tarea sat on sasbs.tarea_id = sat.id 
join auth_user au on sat.responsable_id = au.id 
where sas.nombre = 'Sprint 2'

select * from scrum_app_tarea sat where bloqueadores != ''
