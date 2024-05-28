#PROYECTO ASIGNACIÓN DE CASILLEROS: SECCIÓN EN EL AVA- Se considera que miembros del punto estudiantil ingresarán los datos
"""A versión 1.0 falta: 
   -try for para errores de tipeo, por si ponen texto en vez de números y viceversa (linea 7)
   -funcion para que el rango de fecha exista (que no pueda poner mes 94 por ejemplo en el mes) (linea 10)
   -dar tiempo restante en español (linea 22)"""

usuario= input("Nombre del alumno: ");
casillero_asignado=input("Casillero asignado: ");
print("A continuación ingrese día, mes y año en el que el alumno debe entregar el casillero");
dia_entrega=int(input("Día: ")); mes_entrega=int(input("Mes: ")); year_entrega=int(input("Año: "));


import datetime;
dia_de_hoy= datetime.datetime.now();
fecha_entrega = datetime.datetime(year_entrega, mes_entrega, dia_entrega);
tiempo_restante= fecha_entrega-dia_de_hoy;

with open("PANTALLA.txt", "w") as seccion_AVA:
    seccion_AVA.write(f"ALUMNO: {usuario}");
    seccion_AVA.write(f"\n\nCASILLERO ASIGNADO: {casillero_asignado}");
    seccion_AVA.write(f"\n\nFECHA ENTREGA: {fecha_entrega}");
    seccion_AVA.write(f"\n\nTiempo restante para devolver el casillero: \n{str(tiempo_restante)}");
