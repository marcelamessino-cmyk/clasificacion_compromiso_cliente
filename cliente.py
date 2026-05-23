#clientes py
sesiones = [ 
    [101,210,12],
    [102,45,2],
    [103,90,5],
    [104,109,7],
    [105,300,15]

]# funcio de clasificacio
def clasificacion (sesion):
    if sesion[1] < 50:
        return "Bajo"
    elif sesion[1] < 150:
        return "Medio"
    else:
        return "Alto"
#mostrar resultados
for sesion in sesiones:
    categoria = clasificacion(sesion)
    print(f"Cliente {sesion[0]}: Categoria {categoria}")
    
