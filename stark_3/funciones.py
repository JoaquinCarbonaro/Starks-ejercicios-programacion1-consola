'''
nombre: Joaquin
apellido: Carbonaro
'''
def stark_normalizar_datos(lista:list)->bool:
    '''
    Normaliza los datos de una lista (solo keys que representan datos numéricos)
    Parámetros: lista
    Devuelve: True si los datos se normalizaron correctamente, False en caso contrario
             y un printeo en ambos casos.
    '''
    datos_normalizados = False
    for personaje in lista:
        if type(personaje["fuerza"]) != int:
            try:
                personaje["fuerza"] = int(personaje["fuerza"])
                datos_normalizados = True
            except ValueError:
                pass

        if type(personaje["altura"]) != float:
            try:
                personaje["altura"] = float(personaje["altura"])
                datos_normalizados = True
            except ValueError:
                pass

        if type(personaje["peso"]) != float:
            try:
                personaje["peso"] = float(personaje["peso"])
                datos_normalizados = True
            except ValueError:
                pass
        
    if datos_normalizados:
        print("Datos Normalizados")
    else:
        print("Hubo un error al normalizar los datos.\n\
Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente.")

    return datos_normalizados


def obtener_dato(heroe:dict, clave:str)->str:
    '''
    Obtiene un dato específico de un héroe.
    Parámetros: heroe (diccionario), clave (string)
    Devuelve: El valor del dato si existe, False en caso contrario.
    '''
    if type(heroe) == dict and "nombre" in heroe:
        if clave in heroe:
            return heroe[clave]
    return False


def obtener_nombre(heroe:dict)-> str:
    '''
    Obtiene el nombre de un héroe.
    Parámetros: heroe (diccionario)
    Devuelve: El nombre del héroe si existe, False en caso contrario.
    '''
    nombre = obtener_dato(heroe, "nombre")
    if nombre:
        return f"Nombre: {nombre}"
    return False


def obtener_nombre_y_dato(heroe:dict, dato:str)-> str:
    '''
    Obtiene el nombre de un héroe y un dato específico.
    Parámetros: heroe (diccionario), dato (string)
    Devuelve: string que combina el nombre y el dato si ambos existen, False en caso contrario.
    '''
    nombre = obtener_dato(heroe, "nombre")
    valor = obtener_dato(heroe, dato)
    if nombre and valor:
        return f"{nombre} | {dato}: {valor}"
    return False


def obtener_maximo(lista:list, clave:str)->float:
    '''
    Obtiene el valor máximo de una clave específica en una lista.
    Parámetros: lista (lista de diccionarios), clave (string)
    Devuelve: El valor máximo encontrado o False si no se encuentra ningún valor.
    '''
    maximo = None
    if lista and type(lista) == list:
        for heroe in lista:
            valor = obtener_dato(heroe, clave)
            if type(valor) in (int, float):
                if (maximo == None) or (valor > maximo):
                    maximo = valor
        return maximo
    else:
        return False
    

def obtener_minimo(lista:list, clave:str)->float:
    '''
    Obtiene el valor mínimo de una clave específica en una lista.
    Parámetros: lista (lista de diccionarios), clave (string)
    Devuelve: El valor mínimo encontrado o False si no se encuentra ningún valor.
    '''
    minimo = None
    if lista and type(lista) == list:
        for heroe in lista:
            valor = obtener_dato(heroe, clave)
            if type(valor) in (int, float):
                if (minimo == None) or (valor < minimo):
                    minimo = valor
        return minimo
    else:
        return False
    

def obtener_dato_cantidad(lista:list, valor:float, clave:str)-> list:
    '''
    Obtiene héroes que tienen un valor específico en una clave dada en una lista.
    Parámetros: lista (lista de diccionarios), valor (float), clave (string)
    Devuelve: Lista de héroes que tienen el valor específico en la clave.
    '''
    heroes_segun_valor = []
    if lista and type(lista) == list:
        for heroe in lista:
            valor_heroe = obtener_dato(heroe, clave)
            if (type(valor_heroe) in (int, float)) and (valor_heroe == valor):
                heroes_segun_valor.append(heroe)
    return heroes_segun_valor


def stark_imprimir_heroes(lista:list):
    '''
    Imprime los datos en una lista.
    Parámetros: lista (lista de diccionarios)
    Devuelve: los datos printeados si existen, False en caso contrario.
    '''
    if lista and type(lista) == list:
        for heroe in lista:
            for item in heroe.items():
                print(f"{item[0]}: {item[1]}")
    else:
        return False


def sumar_dato_heroe(lista:list, clave:str)->float:
    '''
    Suma los valores de una clave específica de héroes en una lista.
    Parámetros: lista (lista de diccionarios), clave (string)
    Devuelve: La suma de los valores de la clave en la lista.
    '''
    suma = 0
    if lista and type(lista) == list:
        for heroe in lista:
            valor = obtener_dato(heroe, clave)
            if type(valor) in (int, float):
                suma += valor
    return suma


def dividir(dividendo:float, divisor:float)->float:
    '''
    Divide dos números.
    Parámetros: dividendo (float), divisor (float)
    Devuelve: El resultado de la división o False si el divisor es cero.
    '''
    if divisor == 0:
        return False
    else:
        resultado = dividendo / divisor
        return resultado


def calcular_promedio(lista:list, clave:str)->float:
    '''
    Calcula el promedio de los valores de una clave específica en una lista.
    Parámetros: lista (lista de diccionarios), clave (string)
    Devuelve: El promedio de los valores de la clave.
    '''
    acumulador = sumar_dato_heroe(lista, clave)
    contador = len(lista)
    promedio = dividir(acumulador, contador)
    return promedio
    

def mostrar_promedio_dato(lista:list, clave:str):
    '''
    Muestra el promedio de los valores de una clave específica en una lista de héroes.
    Parámetros: lista (lista de diccionarios), clave (string)
    Devuelve: Un printeo del promedio de la clave. False si el valor de la clave es de
             tipo int/float o está vacía.
    '''
    promedio = calcular_promedio(lista, clave)
    if (lista) and (type(promedio) in (int, float)):
        return print(f"Promedio {clave}: {promedio:.2f}")
    else:
        return False


def imprimir_menu():
    '''
    Imprime el menú principal de la aplicación Stark.
    Parámetros: Ninguno
    Devuelve: los datos printeados.
    '''
    print("\nMenú de Informes:\n\
    1.Normalizar datos\n\
    2.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\n\
    3.Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n\
    4.Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n\
    5.Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n\
    6.Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n\
    7.Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n\
    8.Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n\
    9.Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n\
    10.Listar todos los superhéroes agrupados por color de ojos.\n\
    11.Listar todos los superhéroes agrupados por tipo de inteligencia\n\
    12.Salir")

def validar_entero(numero_str:str)->bool:
    '''
    Valida si un string representa un número entero.
    Parámetros: numero_str (string)
    Devuelve: True si el string es un número entero, False en caso contrario.
    '''
    if numero_str.isdigit():
        return True
    else:
        return False
    

def stark_menu_principal()->int:
    '''
    Muestra el menú principal y obtiene la opción seleccionada por el usuario.
    Parámetros: Ninguno
    Devuelve: Opción seleccionada por el usuario en formato int.
    '''
    #while True:
    imprimir_menu()
    opcion = input("Ingrese el número de la opción deseada: ").strip()
    if validar_entero(opcion):
        opcion = int(opcion)
        if (opcion >= 1) and (opcion <= 12):
            return opcion
    return False


def stark_marvel_app(lista_personajes:list):
    '''
    Aplicación principal de Stark que interactúa con el usuario y realiza la accion solicitada.
    Parámetros: lista_personajes (lista de diccionarios).
    Devuelve: los datos printeados.
    '''
    datos_normalizados = False
    lista_personaje_nb = []
    lista_personaje_f = []
    lista_personaje_max_altura_f = []
    lista_nombre_max_altura_f  =[]
    lista_personaje_m = []
    lista_personaje_max_altura_m = []
    lista_nombre_max_altura_m =[]
    lista_personaje_m = []
    lista_personaje_min_fuerza_m = []
    lista_nombre_min_fuerza_m =[]
    lista_personaje_nb = []
    lista_personaje_min_fuerza_nb = []
    lista_nombre_min_fuerza_nb =[]
    lista_personaje_nb = [] 
    lista_ojos_contar = []
    lista_pelo_contar = []
    lista_ojos_agrupar = []
    lista_inteligencia_agrupar = []

    while True:
        opcion = stark_menu_principal()

        if opcion == 1:
            stark_normalizar_datos(lista_personajes)
            datos_normalizados = True

        elif datos_normalizados:
            if opcion == 2:
                lista_personaje_nb = obtener_personaje_genero(lista_personajes, "NB")
                lista_nombre_nb = filtrar_nombre(lista_personaje_nb)
                stark_imprimir_heroes(lista_nombre_nb)

            elif opcion == 3:
                lista_personaje_f = obtener_personaje_genero(lista_personajes, "F")
                max_altura_f = obtener_maximo(lista_personaje_f, "altura")
                lista_personaje_max_altura_f = obtener_dato_cantidad(lista_personajes, max_altura_f, "altura")
                lista_nombre_max_altura_f = filtrar_nombre(lista_personaje_max_altura_f)
                stark_imprimir_heroes(lista_nombre_max_altura_f)

            elif opcion == 4:
                lista_personaje_m = obtener_personaje_genero(lista_personajes, "M")
                max_altura_m = obtener_maximo(lista_personaje_m, "altura")
                lista_personaje_max_altura_m = obtener_dato_cantidad(lista_personajes, max_altura_m, "altura")
                lista_nombre_max_altura_m = filtrar_nombre(lista_personaje_max_altura_m)
                stark_imprimir_heroes(lista_nombre_max_altura_m)

            elif opcion == 5:
                lista_personaje_m = obtener_personaje_genero(lista_personajes, "M")
                min_fuerza_m = obtener_minimo(lista_personaje_m, "fuerza")
                lista_personaje_min_fuerza_m = obtener_dato_cantidad(lista_personajes, min_fuerza_m, "fuerza")
                lista_nombre_min_fuerza_m = filtrar_nombre(lista_personaje_min_fuerza_m)
                stark_imprimir_heroes(lista_nombre_min_fuerza_m)

            elif opcion == 6:
                lista_personaje_nb = obtener_personaje_genero(lista_personajes, "NB")
                min_fuerza_nb = obtener_minimo(lista_personaje_nb, "fuerza")
                lista_personaje_min_fuerza_nb = obtener_dato_cantidad(lista_personajes, min_fuerza_nb, "fuerza")
                lista_nombre_min_fuerza_nb = filtrar_nombre(lista_personaje_min_fuerza_nb)
                stark_imprimir_heroes(lista_nombre_min_fuerza_nb)

            elif opcion == 7:
                lista_personaje_nb = obtener_personaje_genero(lista_personajes, "NB")
                mostrar_promedio_dato(lista_personaje_nb, "fuerza")
                
            elif opcion == 8:
                lista_ojos_contar = contar_agrupar_caracteristica(lista_personajes, "color_ojos", "contar")
                lista_filtrada_contar = filtra_contar_agrupar(lista_ojos_contar, "contar")
                stark_imprimir_heroes(lista_filtrada_contar)

            elif opcion == 9:
                lista_pelo_contar = contar_agrupar_caracteristica(lista_personajes, "color_pelo", "contar")
                lista_filtrada_contar = filtra_contar_agrupar(lista_pelo_contar, "contar")
                stark_imprimir_heroes(lista_filtrada_contar)
                               
            elif opcion == 10:
                lista_ojos_agrupar = contar_agrupar_caracteristica(lista_personajes, "color_ojos", "agrupar")
                lista_filtrada_agrupar = filtra_contar_agrupar(lista_ojos_agrupar, "agrupar")
                stark_imprimir_heroes(lista_filtrada_agrupar)

            elif opcion == 11:
                lista_inteligencia_agrupar = contar_agrupar_caracteristica(lista_personajes, "inteligencia", "agrupar")
                lista_filtrada_agrupar = filtra_contar_agrupar(lista_inteligencia_agrupar, "agrupar")
                stark_imprimir_heroes(lista_filtrada_agrupar)

            elif opcion == 12:
                print("Saliendo del programa. Hasta luego.")
                break
            
            else:
                print("Opción no válida. Por favor, elija una opción válida.")
        else:
            print("Debe seleccionar la opción 1 (Normalizar datos) primero.")


def obtener_personaje_genero(lista:list, genero:str)->list:
    '''
    Filtra personajes por género y devuelve una lista de personajes del género especificado.
    Parámetros: lista (lista de diccionarios), genero (string)
    Devuelve: Una lista (de diccionarios) de personajes.
    '''
    personaje_genero = []
    for personaje in lista:
        if personaje["genero"] == genero:
            personaje_genero.append(personaje)
    return personaje_genero


def filtrar_nombre(lista:list)->list:
    '''
    Retorna una lista con el nombre de cada personaje en forma de lista (de diccionarios).
    Parámetros: lista (lista de diccionarios)
    Devuelve: Una lista de diccionarios con el nombre de los personajes.
    '''
    lista_nombres = []
    for dato in lista:
        nombre = obtener_nombre(dato)
        if nombre:
            nombre_sin_prefijo = nombre.split(":")[1].strip()  # split(":") divide la cadena en dos.
            lista_nombres.append({"Nombre": nombre_sin_prefijo})
    return lista_nombres
    

def normalizar_tipografia(lista: list, clave: str):
    '''
    Normaliza la tipografía de los valores de una clave en los diccionarios de la lista.
    Parámetros: lista (lista de diccionarios), clave (string)
    Devuelve: lista con valores en mayuscula y sin espacios
    '''
    for personaje in lista:
        if (clave in personaje) and (type(personaje[clave]) == str):
            personaje[clave] = personaje[clave].strip().upper()


def contar_agrupar_caracteristica(lista: list, caracteristica: str, contar_agrupar:str) -> list:
    '''
    Realiza conteo o agrupación de personajes por una característica.
    Parámetros: lista (lista de diccionarios), caracteristica (string), contar_agrupar (string)
    Devuelve: Una lista de diccionarios con información de la característica.
    '''
    lista_diccionarios = []

    normalizar_tipografia(lista, "color_pelo")
    normalizar_tipografia(lista, "color_ojos")
    normalizar_tipografia(lista, "inteligencia")

    for personaje in lista:
        caracteristica_valor = personaje[caracteristica]
        encontrado = False

        for diccionario in lista_diccionarios:
            if diccionario['Caracteristica'] == caracteristica_valor:
                if contar_agrupar == "contar":
                    diccionario['Cantidad'] += 1
                elif contar_agrupar == "agrupar":
                    diccionario['Superhéroes'].append(personaje["nombre"])
                encontrado = True
                break
        
        if not encontrado:
            nuevo_diccionario = {'Caracteristica': caracteristica_valor, 'Cantidad': 1, 'Superhéroes': []}
            if contar_agrupar == "agrupar":
                nuevo_diccionario['Superhéroes'].append(personaje["nombre"])
            
            lista_diccionarios.append(nuevo_diccionario)

    return lista_diccionarios


def filtra_contar_agrupar(lista_caracteristica: list, contar_agrupar: str) -> list:
    '''
    Realiza ordenamiento de informacion segun conteo o agrupación de características.
    Parámetros: lista_caracteristica (lista de diccionarios), contar_agrupar (string)
    Devuelve: Una lista de diccionarios con información de la característica segun se pida contar o agrupar.
    '''
    dic_caracteristica = []

    for tipo in lista_caracteristica:
        diccionario = {"Caracteristica": tipo["Caracteristica"]}

        if contar_agrupar == "contar":
            diccionario["Cantidad"] = tipo["Cantidad"]

        elif contar_agrupar == "agrupar":
            diccionario["Nombre"] = tipo["Superhéroes"]

        dic_caracteristica.append(diccionario)

    return dic_caracteristica