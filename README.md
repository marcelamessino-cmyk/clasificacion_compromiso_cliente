# clasificacion de compromiso de cliente
proyecto desarrollado en python para almacenar datos de sesiones y clasificar el nivel de compromiso segun la duracion.
# datos iniciales 
matriz con 5 registros:[ID clientes, duracion (segundos),clics]
python
sesiones = [
[101,210,12]
[102,45,2]
[103,90,5]
[104,109,7]
[105,300,15]
]
# logica de clasificacion
Bajo: menos de 50 segundos
Medio: entre 50 y 149 segundo
Alto: 150 segundo o mas 
# ejecucion python cliente.py
# salida en espera 
cliente 101:categoria Alto
cliente 102: categoria Bajo
cliente 103: categoria Medio
cliente 104 categoria Alto
