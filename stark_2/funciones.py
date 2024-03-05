'''
nombre: Joaquin
apellido: Carbonaro
'''
def normalizar_datos(lista:list):
    '''
    Normaliza los datos ("altura", "peso" y "fuerza") de una lista, convirtiendo en números
    (float o int), o en None si los datos no son válidos.
    Parámetros: lista (list)
    Devuelve: Ningún valor explícito, pero modifica la lista de personajes en su lugar.
    '''
    for personaje in lista:
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


def mostrar_menu()->str:
    '''
    Muestra un menú y solicita al usuario una opción.
    Parámetros: Ninguno
    Devuelve: La opción ingresada por el usuario como un string.
    '''
    print("\nMenú:\n\
    A. Imprimir nombres de superhéroes de género NB\n\
    B. Superhéroe más alto de género F\n\
    C. Superhéroe más alto de género M\n\
    D. Superhéroe más débil de género M\n\
    E. Superhéroe más débil de género NB\n\
    F. Fuerza promedio de superhéroes de género NB\n\
    G. Cantidad de superhéroes por color de ojos\n\
    H. Cantidad de superhéroes por color de pelo\n\
    I. Superhéroes agrupados por color de ojos\n\
    J. Superhéroes agrupados por tipo de inteligencia\n\
    S. Salir\n")
    opcion = input("Ingrese la opción deseada: ").strip().upper()
    return opcion


def buscar_superheroes_genero(lista: list, genero: str) -> list:
    '''
    Busca y devuelve una lista de un género específico.
    Parámetros: lista (list), genero (str)
    Devuelve: Una lista de diccionarios.
    '''
    superheroes_filtrados_genero = []
    
    for personaje in lista:
        if personaje["genero"] == genero:
            superheroes_filtrados_genero.append(personaje)
    
    return superheroes_filtrados_genero


def imprimir_superheroes_nb(lista:list):
    '''
    Imprime los nombres de los superhéroes de género NB.
    Parámetros: lista (list)
    Devuelve: los datos printeados
    '''
    print("Superhéroes de género NB:")
    for personaje in lista:
        print(personaje["nombre"])


def encontrar_maximo_minimo(lista: list, tipo: str, max_min: str) -> list: #tipo=altura/fuerza
    '''
    Encuentra el valor maximo o minimo (según el tipo) y devuelve una lista con uno o varios 
    resultados en caso de existir varios con el mismo valor.
    Parámetros: lista (list), tipo (str), max_min (str)
    Devuelve: Una lista de diccionarios.
    '''
    dic_min_max = lista[0]
    resultado = []
    
    for personaje in lista:
        if max_min == "maximo" and (personaje[tipo] > dic_min_max[tipo]):
            dic_min_max = personaje
            resultado = [dic_min_max]
        elif max_min == "minimo" and (personaje[tipo] < dic_min_max[tipo]):
            dic_min_max = personaje
            resultado = [dic_min_max]
        elif personaje[tipo] == dic_min_max[tipo]:
            resultado.append(personaje)

    return resultado


def imprimir_superheroe_maximo_minimo(lista_min_max:list, genero: str, tipo: str):
    '''
    Imprime el valor maximo o minimo (según el tipo) de un género específico.
    Parámetros: lista_min_max (list), genero (str), tipo (str)
    Devuelve: los datos printeados
    '''
    if tipo == "altura":
        print(f"El superhéroe más alto de género {genero} es:")
    else:
        print(f"El superhéroe más débil de género {genero} es:")
    
    for personaje in lista_min_max:
        print(f"- {personaje['nombre']} ({tipo}: {personaje[tipo]})")


def calcular_fuerza_promedio(lista: list) -> float:
    '''
    Calcula el promedio de la fuerza.
    Parámetros: lista (list)
    Devuelve: El promedio de la fuerza en formato float.
    '''
    acumulador_fuerza = 0
    contador_fuerza = 0
    
    for personaje in lista:
        acumulador_fuerza += personaje["fuerza"]
        contador_fuerza += 1
    
    if contador_fuerza == 0:
        promedio_fuerza = 0
    else:
        promedio_fuerza = acumulador_fuerza / contador_fuerza
    return promedio_fuerza


def imprimir_fuerza_promedio(promedio:float):
    '''
    Imprime el valor del promedio de fuerza en formato float de dos decimales.
    Parámetros: promedio (float)
    Devuelve: los datos printeados
    '''
    print(f"La fuerza promedio de los superhéroes de género NB es: {promedio:.2f}.")


def normalizar_tipografia(lista: list, clave: str):
    '''
    Normaliza la tipografía de los valores de una clave en los diccionarios de la lista.
    Parámetros: lista (lista de diccionarios), clave (string)
    Devuelve: lista con valores en mayuscula y sin espacios
    '''
    for personaje in lista:
        if (clave in personaje) and (type(personaje[clave]) == str):
            personaje[clave] = personaje[clave].strip().upper()


def contar_agrupar_caracteristica(lista:list, caracteristica:str, contar_agrupar:str)->dict:
    '''
    Cuenta o agrupa por una característica específica (color_ojos/color_pelo/inteligencia) y 
    devuelve un diccionario con los resultados.
    Parámetros: lista (list), caracteristica (str), contar_agrupar (str)
    Devuelve: Un diccionario que contiene la característica como clave y la cantidad o una 
            lista de nombres de superhéroes según la operación seleccionada.
    '''
    dic_caracteristica = {}

    normalizar_tipografia(lista, "color_pelo")
    normalizar_tipografia(lista, "color_ojos")
    normalizar_tipografia(lista, "inteligencia")
    
    for personaje in lista:
        if contar_agrupar == "contar":
            if personaje[caracteristica] in dic_caracteristica:
                dic_caracteristica[personaje[caracteristica]] += 1
            else:
                dic_caracteristica[personaje[caracteristica]] = 1
        
        elif contar_agrupar == "agrupar":
            if personaje[caracteristica] in dic_caracteristica:
                dic_caracteristica[personaje[caracteristica]].append(personaje["nombre"])
            else:
                dic_caracteristica[personaje[caracteristica]] = [personaje["nombre"]]
    
    return dic_caracteristica


def imprimir_contar_agrupar_caracteristica(dic_caracteristica: dict, caracteristica:str):
    '''
    Imprime los resultados de contar o agrupar superhéroes por una característica específica.
    Parámetros: dic_caracteristica (dict), caracteristica (str)
    Devuelve: los datos printeados
    '''
    for tipo in dic_caracteristica:
        if caracteristica == "color_ojos":
            print(f"Color de ojos '{tipo}': {dic_caracteristica[tipo]}")
        elif caracteristica == "color_pelo":
            print(f"Color de pelo '{tipo}': {dic_caracteristica[tipo]}")
        else:
            print(f"Inteligencia '{tipo}': {dic_caracteristica[tipo]}")