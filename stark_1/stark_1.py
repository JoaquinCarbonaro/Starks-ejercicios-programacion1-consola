'''
nombre: Joaquin
apellido: Carbonaro

Luego de analizar el set de datos correspondiente resolver el Desafío #01:
A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino
NOTA: Se debe construir un menú en el que se sea posible acceder a cada una de
las opciones (A-E)
'''

from data_stark import lista_personajes

for personaje in lista_personajes:
        try:
            personaje["altura"] = float(personaje["altura"])
        except :
            personaje["altura"] = None
        try:
            personaje["peso"] = float(personaje["peso"])
        except :
            personaje["peso"] = None
        try:
            personaje["fuerza"] = int(personaje["fuerza"])
        except :
            personaje["fuerza"] = None

while True:
    print("\nMenú:\n\
    A. Imprimir todos los datos de cada superhéroe\n\
    B. Mostrar identidad y peso del superhéroe más fuerte (MÁXIMO)\n\
    C. Mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)\n\
    D. Mostrar el peso promedio de superhéroes masculinos (PROMEDIO)\n\
    E. Mostrar superhéroes con fuerza superior al promedio de las mujeres\n\
    S. Salir")

    opcion = input("Ingrese la opción deseada: ").strip().upper()

    if opcion == "A":
        for personaje in lista_personajes:
            for item in personaje.items():
                print(f"{item[0]}: {item[1]}")
            print()
    
    elif opcion == "B":
        superheroe_mas_fuerte = lista_personajes[0]
        for personaje in lista_personajes:
            if personaje["fuerza"] > superheroe_mas_fuerte["fuerza"]:
                superheroe_mas_fuerte = personaje
        print(f"Identidad del superhéroe más fuerte: {superheroe_mas_fuerte['identidad']}")
        print(f"Peso del superhéroe más fuerte: {float(superheroe_mas_fuerte['peso']):.2f}")

    elif opcion == "C":
        superheroe_mas_bajo = lista_personajes[0]
        for personaje in lista_personajes:
            if personaje["altura"] < superheroe_mas_bajo["altura"]:
                superheroe_mas_bajo = personaje
        print(f"Nombre del superhéroe más bajo: {superheroe_mas_bajo['nombre']}")
        print(f"Identidad del superhéroe más bajo: {superheroe_mas_bajo['identidad']}")
        
    elif opcion == "D":
        acumulador_peso = 0
        contador_masculino = 0
        for personaje in lista_personajes:
            if personaje["genero"] == "M":
                acumulador_peso += personaje["peso"]
                contador_masculino += 1
        if contador_masculino > 0:
            peso_promedio = acumulador_peso / contador_masculino
            print(f"Peso promedio de superhéroes masculinos: {peso_promedio:.2f}")
        else:
            print("No se encontraron superhéroes masculinos.")

    elif opcion == "E":
            acumulador_fuerza = 0
            contador_femenino = 0
            for personaje in lista_personajes:
                if personaje["genero"] == "F":
                    acumulador_fuerza += personaje["fuerza"]
                    contador_femenino += 1
            if contador_femenino > 0:
                fuerza_promedio_f = acumulador_fuerza / contador_femenino
                print(f"Los superhéroes cuales su fuerza supera a la fuerza promedio ({fuerza_promedio_f:.2f}) de todas las superhéroes de género femenino son:")
                for personaje in lista_personajes:
                    if personaje["fuerza"] > fuerza_promedio_f:
                        print(f"Nombre: {personaje['nombre']}, Peso: {personaje['peso']:.2f}")
            else:
                print("No se encontraron superhéroes de género femenino.")

    elif opcion == "S":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")