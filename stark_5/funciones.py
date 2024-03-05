import json
import csv

#1.1.#######################################################################################################################

def leer_archivo(nombre_archivo:str)-> str:    
    """
    Lee el contenido de un archivo especificado.
    Parámetros:
    - nombre_archivo (str): El nombre y la extensión del archivo a leer.
    Retorna:
    - str: El contenido del archivo como una cadena de texto si la lectura es exitosa.
           False en caso de error, con impresión del mensaje de error.
    """
        #intenta abrir el archivo en modo lectura y codificarlo en UTF-8.
        # with open: Se utiliza para abrir un archivo y asegurarse de que se cierre 
        # correctamente una vez que se haya terminado de trabajar con él.
        # "r": modo en el que se abre el archivo. En este caso, 'r' indica que el archivo 
        # se abre en modo de solo lectura. No se pueden realizar cambios en él
        # as archivo: asigna el archivo que se ha abierto a una variable llamada 'archivo'. 
        # Esta variable se puede utilizar para realizar operaciones de lectura en el archivo
    try:  
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:  
            return archivo.read()  #devuelve el contenido del archivo como una cadena.
    except FileNotFoundError:  #si el archivo no se encuentra en la ruta especificada.
        print(f"El archivo {nombre_archivo} no fue encontrado.")  
        return False 
    except PermissionError:  #si no se tienen los permisos necesarios para acceder al archivo.
        print(f"No tienes permiso para abrir el archivo {nombre_archivo}.")  
        return False  
    except Exception:  #cualquier otra excepción que pueda ocurrir durante la lectura del archivo.
        # Imprime un mensaje de error genérico 
        print(f"Se ha producido un error inesperado")  
        return False  

#1.2.#######################################################################################################################

def guardar_archivo(nombre_archivo: str, contenido: str) -> bool:
    """
    Guarda el contenido en un archivo especificado.
    Parámetros:
    - nombre_archivo (str): El nombre y la extensión del archivo a guardar.
    - contenido (str): El contenido a guardar en el archivo.
    Retorna:
    - bool: True si no hay errores al guardar el archivo, False en caso contrario.
    """
    try:
        with open(nombre_archivo, 'w+', encoding='utf-8') as archivo:
            # Abre el archivo en modo escritura y lectura ('w+') y codifica el contenido en UTF-8.
            archivo.write(contenido)  #escribe el contenido en el archivo.
            print(f"Se creó el archivo: {nombre_archivo}")  
            return True 
    except Exception:
        #excepción que pueda ocurrir durante el proceso de escritura.
        print(f"Error al crear el archivo: {nombre_archivo}") 
        return False

#1.3.#######################################################################################################################

def generar_csv(nombre_archivo: str, lista_recibida: list) -> bool:
    """
    Genera un archivo CSV a partir de una lista de superhéroes.
    Parameters:
    - nombre_archivo (str): El nombre y extensión del archivo CSV.
    - lista_heroes (list): La lista de superhéroes, cada uno representado como un diccionario.
    Returns:
    - bool: True si se generó y guardó el archivo correctamente, False si la lista está vacía o si se produce un error.
    """
    #verifica que la lista de superhéroes no esté vacía y sea del tipo lista.
    if type(lista_recibida) == list and len(lista_recibida) == 0:
        return False
    #título del archivo CSV.
    csv_string = "Nombre,Identidad,Empresa,Altura,Peso,Género,Color_ojos,Color_pelo,fuerza,Inteligencia\n"  

    for personaje in lista_recibida:
        #agrega la información de cada superhéroe al string en formato CSV.
        csv_string += f"{personaje['nombre']},{personaje['identidad']},{personaje['empresa']},\
{personaje['altura']},{personaje['peso']},{personaje['genero']},{personaje['color_ojos']},\
{personaje['color_pelo']},{personaje['fuerza']},{personaje['inteligencia']}\n"

    
    #llama a la función guardar_archivo para guardar el string en un archivo CSV.
    return guardar_archivo(nombre_archivo, csv_string)

#1.4.#######################################################################################################################

def leer_csv(nombre_archivo: str) -> list:
    """
    Lee un archivo CSV y genera una lista de diccionarios de superhéroes.
    Parameters:
    - nombre_archivo (str): El nombre y extensión del archivo CSV.
    Returns:
    - list: Lista de diccionarios de superhéroes si el archivo existe, False en caso contrario.
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lista_superheroes = []  #lista vacía para almacenar los superhéroes.
            encabezados = None  #inicializa la variable 'encabezados' como None para almacenar los encabezados del CSV.
            primera_linea = True  #bandera que verifica si se trata de la primera línea del archivo.

            for linea in archivo:  #itera sobre cada línea del archivo.
                valores = linea.strip().split(',')  #divide la línea en valores separados por comas.
                if primera_linea:  #verifica si es la primera línea del archivo.
                    encabezados = valores  #asigna los encabezados a la variable 'valores'.
                    primera_linea = False  #cambia la bandera a False después de procesar la primera línea.
                else:
                    #crea un diccionario para cada línea basado en los encabezados y los valores correspondientes.
                    heroe = {encabezados[i]: valores[i] for i in range(len(encabezados))}
                    lista_superheroes.append(heroe)  #agrega el diccionario a la lista de superhéroes.

            if encabezados is not None:  #verifica si se han encontrado los encabezados en el archivo.
                return lista_superheroes  #devuelve la lista de superhéroes si se encuentran los encabezados.
            else:
                return False  #devuelve False si no se encuentran los encabezados en el archivo.
    except FileNotFoundError:  #excepción si el archivo no se encuentra.
        print(f"El archivo {nombre_archivo} no fue encontrado.")  
        return False  #devuelve False si ocurre un error de archivo no encontrado.
    except Exception:  #cualquier otra excepción que pueda ocurrir.
        print(f"Se ha producido un error inesperado")  # Imprime un mensaje de error genérico.
        return False  #devuelve False si ocurre un error inesperado.

#1.5.#######################################################################################################################

def generar_json(nombre_archivo: str, lista_recibida: list, nombre_lista: str) -> bool:
    """
    Genera un archivo JSON con la información de los superhéroes.
    Parameters:
    - nombre_archivo (str): El nombre y extensión del archivo JSON.
    - lista_heroes (list): La lista de superhéroes (cada héroe como un diccionario).
    - nombre_lista (str): El nombre de la lista de superhéroes en el diccionario JSON.
    Returns:
    - bool: True si no hubo errores, False en caso contrario.
    """
    #verifica si la lista esta vacía y si es del tipo lista
    if type(lista_recibida) == list and len(lista_recibida) == 0:
        return False
            
    data = {nombre_lista: lista_recibida}
    
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        #escribe el diccionario en el archivo JSON con formato legible.
            json.dump(data, archivo, indent=4)  #indent=4: sangría de 4 espacios

        print(f"Se ha creado el archivo JSON: {nombre_archivo}")  
        return True
    except Exception:
        print(f"Error al crear el archivo JSON: {nombre_archivo}")  
        return False



#1.6.#######################################################################################################################

def leer_json(nombre_archivo: str, nombre_lista: str) -> list:
    """
    Lee un archivo JSON y retorna la lista obtenida.
    Parameters:
    - nombre_archivo (str): El nombre y extensión del archivo a leer (Ruta absoluta o relativa).
    - nombre_lista (str): El nombre de la lista a leer dentro del archivo JSON.
    Returns:
    list or False: La lista obtenida si el archivo existe, False si el archivo no existe.
    """
    try:
        #abre el archivo en modo lectura.
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:  
            data = json.load(archivo)  #carga el contenido del archivo JSON en una variable data.
            #verifica si la clave especificada existe en el diccionario cargado desde el archivo.
            if nombre_lista in data: 
                #devuelve la lista correspondiente a la clave especificada. 
                return data[nombre_lista]  
            else:
                print(f"El nombre de lista '{nombre_lista}' no se encuentra en el archivo JSON.")
                return False  #devuelve False si el nombre de lista no se encuentra en el archivo.

    except FileNotFoundError:  #excepción si el archivo no se encuentra.
        print(f"El archivo {nombre_archivo} no fue encontrado.")  
        return False  #devuelve False si ocurre un error de archivo no encontrado.
    except Exception:  #cualquier otra excepción que pueda ocurrir.
        print(f"Se ha producido un error inesperado")  
        return False  #False si ocurre un error inesperado.

#2.1.#######################################################################################################################

#METODO BURBUJEO - SORT
def ordenar_heroes_ascendente_csv_json(archivo:str, clave:str):
    """
    Ordena la lista de héroes por una clave numérica de manera ascendente.
    Parameters:
    - lista_heroes (list): La lista de héroes (cada héroe representado como un diccionario).
    - clave (str): La clave por la cual se realizará la ordenación (altura, peso o fuerza).
    Returns:
    list: La lista de héroes ordenada por la clave numérica especificada.
    """
    try:
        # Determina el tipo de archivo basándose en la extensión
        extension = archivo.split('.')[-1].lower()

        if extension == 'csv':
            # Lee el archivo CSV
            with open(archivo, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                lista_recibida = list(reader)

            # Verifica si la lista está vacía
            if not lista_recibida:
                print(f"La lista de héroes en {archivo} está vacía.")
                return []

            # Verifica si la clave es válida
            if clave not in lista_recibida[0]:
                print(f"La clave {clave} no es válida.")
                return lista_recibida

            # Verifica si el valor correspondiente es numérico
            if not all(str(item[clave]).replace(".", "").replace(",", "").isdigit() or str(item[clave]) == "" for item in lista_recibida):
                print(f"El valor correspondiente a la clave {clave} no es numérico.")
                return lista_recibida

            # Convierte los valores numéricos a float para ordenar correctamente
            for item in lista_recibida:
                if item[clave]:
                    item[clave] = float(str(item[clave]).replace(",", ""))

            # Ordena la lista de héroes por burbujeo
            n = len(lista_recibida)
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if lista_recibida[j][clave] > lista_recibida[j + 1][clave]:
                        lista_recibida[j], lista_recibida[j + 1] = lista_recibida[j + 1], lista_recibida[j]

        elif extension == 'json':
            # Lee el archivo JSON
            with open(archivo, 'r', encoding='utf-8') as jsonfile:
                lista_recibida = json.load(jsonfile)
            
            # Verifica si la clave es válida
            if clave not in lista_recibida['lista_personajes'][0]:
                print(f"La clave {clave} no es válida.")
                return lista_recibida

            # Verifica si el valor correspondiente es numérico
            if not all(str(item[clave]).replace(".", "").replace(",", "").isdigit() or str(item[clave]) == "" for item in lista_recibida['lista_personajes']):
                print(f"El valor correspondiente a la clave {clave} no es numérico.")
                return lista_recibida

            # Convierte los valores numéricos a float para ordenar correctamente
            for item in lista_recibida['lista_personajes']:
                if item[clave]:
                    item[clave] = float(str(item[clave]).replace(",", ""))

            # Ordena la lista de héroes por la clave especificada de manera descendente
            lista_recibida['lista_personajes'].sort(key=lambda x: x[clave])

        else:
            print(f"Formato de archivo no compatible: {extension}")
            return []

        return lista_recibida

    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
        return []
    except Exception:
        print(f"Se ha producido un error inesperado")
        return []

#2.2.#######################################################################################################################

#METODO SORT
def ordenar_heroes_descendente_csv_json(archivo:str, clave:str):
    """
    Ordena la lista de héroes por una clave numérica de manera descendente.
    Parameters:
    - lista_heroes (list): La lista de héroes (cada héroe representado como un diccionario).
    - clave (str): La clave por la cual se realizará la ordenación (altura, peso o fuerza).
    Returns:
    list: La lista de héroes ordenada por la clave numérica especificada de manera descendente.
    """
    try:
        # Determina el tipo de archivo basándose en la extensión
        extension = archivo.split('.')[-1].lower()

        if extension == 'csv':
            # Lee el archivo CSV
            with open(archivo, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                lista_recibida = list(reader)
            
            # Verifica si la lista está vacía
            if not lista_recibida:
                print(f"La lista de héroes en {archivo} está vacía.")
                return []

            # Verifica si la clave es válida
            if clave not in lista_recibida[0]:
                print(f"La clave {clave} no es válida.")
                return lista_recibida

            # Verifica si el valor correspondiente es numérico
            if not all(str(item[clave]).replace(".", "").replace(",", "").isdigit() or str(item[clave]) == "" for item in lista_recibida):
                print(f"El valor correspondiente a la clave {clave} no es numérico.")
                return lista_recibida

            # Convierte los valores numéricos a float para ordenar correctamente
            for item in lista_recibida:
                if item[clave]:
                    item[clave] = float(str(item[clave]).replace(",", ""))

            # Ordena la lista de héroes por la clave especificada de manera descendente
            lista_recibida.sort(key=lambda x: x[clave], reverse=True)

        elif extension == 'json':
            # Lee el archivo JSON
            with open(archivo, 'r', encoding='utf-8') as jsonfile:
                lista_recibida = json.load(jsonfile)
            
            # Verifica si la clave es válida
            if clave not in lista_recibida['lista_personajes'][0]:
                print(f"La clave {clave} no es válida.")
                return lista_recibida

            # Verifica si el valor correspondiente es numérico
            if not all(str(item[clave]).replace(".", "").replace(",", "").isdigit() or str(item[clave]) == "" for item in lista_recibida['lista_personajes']):
                print(f"El valor correspondiente a la clave {clave} no es numérico.")
                return lista_recibida

            # Convierte los valores numéricos a float para ordenar correctamente
            for item in lista_recibida['lista_personajes']:
                if item[clave]:
                    item[clave] = float(str(item[clave]).replace(",", ""))

            # Ordena la lista de héroes por la clave especificada de manera descendente
            lista_recibida['lista_personajes'].sort(key=lambda x: x[clave], reverse=True)

        else:
            print(f"Formato de archivo no compatible: {extension}")
            return []

        return lista_recibida

    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
        return []
    except Exception:
        print(f"Se ha producido un error inesperado")
        return []

#2.3.#######################################################################################################################

def ordenar_heroes_usuario(archivo:str, clave:str):
    """
    Ordena la lista de héroes por una clave numérica, permitiendo al usuario elegir
    si desea ordenar de manera ascendente o descendente.
    Parameters:
    - lista_heroes (list): La lista de héroes (cada héroe representado como un diccionario).
    Returns:
    list: La lista de héroes ordenada por la clave numérica especificada y el orden elegido por el usuario.
    """
    try:
        while True:
            orden = input("Ingrese 'asc' para ordenar de manera ascendente o 'desc' para ordenar de manera descendente: ").lower()
            if orden == 'asc' or orden == 'desc':
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        if orden == 'asc':
            return ordenar_heroes_ascendente_csv_json(archivo, clave) 
        elif orden == 'desc':
            return ordenar_heroes_descendente_csv_json(archivo, clave)  
    except Exception:  
        print(f"Se produjo un error inesperado")  
        return archivo  

#3.#########################################################################################################################

def imprimir_menu():
    print("\nMenú de Informes:\n\
    1. Normalizar datos\n\
    2. Generar CSV (Guardar la lista generada en otra variable)\n\
    3. Listar heroes del archivo CSV ordenados por altura ASC (Validar si el mismo existe)\n\
    4. Generar JSON (Guardar la lista generada en otra variable)\n\
    5. Listar heroes del archivo JSON ordenados por peso DESC (Validar si el mismo existe)\n\
    6. Ordenar Lista por fuerza (usuario ingresa tipo de orden: ASC o DESC)\n\
    7. Salir")

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
    opcion = input("Seleccione una opción: ").strip()
    if validar_entero(opcion):
        opcion = int(opcion)
        if (opcion >= 1) and (opcion <= 7):
            return opcion
    return False

def stark_marvel_app(lista_personajes:list):
    """
    Función principal de la app, donde están aplicadas las funciones anteriores para
    que cada opción funcione y esté acorde con lo que pide el menú
    Parametros: lista recibida
    Devuelve: las respuestas pedidas por el menú
    """
    lista_generar_csv = [] 
    heroes_asc_altura = []
    lista_generar_json = []
    heroes_desc_peso = []
    heroes_ord_fuerza = []

    datos_normalizados = False  #bandera para verificar si los datos están normalizados
    while True:
        opcion = stark_menu_principal()  
        if opcion == 1:
            stark_normalizar_datos(lista_personajes)
            datos_normalizados = True  #normaliza los datos          

        elif datos_normalizados:
            if opcion == 2:
                #opción 2: Generar CSV (Guardar la lista generada en otra variable)
                lista_generar_csv = generar_csv("data_stark.csv", lista_personajes)
                if lista_generar_csv:
                    print(f"Se generó el archivo correctamente.")
                else:
                    print("La lista de superhéroes está vacía.")            
            
            elif opcion == 3:  
                # Llama a la función para ordenar héroes por altura
                archivo_csv = 'data_stark.csv'
                clave_ordenamiento = 'Altura'
                heroes_asc_altura = ordenar_heroes_ascendente_csv_json(archivo_csv, clave_ordenamiento)
                
                # Imprime la lista ordenada por altura
                if heroes_asc_altura:
                    print(f"\nHéroes ordenados por altura (ASC):")
                    for heroe in heroes_asc_altura:
                        print(heroe)
                else:
                    print("El archivo no existe")
            
            elif opcion == 4:
                #opción 4: Generar JSON (Guardar la lista generada en otra variable)
                lista_generar_json = generar_json("data_stark.json", lista_personajes, "lista_personajes")
                if lista_generar_json:
                    print(f"Se generó el archivo JSON correctamente.")
                else:
                    print("La lista de superhéroes está vacía.")

            elif opcion == 5:
                # Llama a la función para ordenar héroes por altura
                archivo_json = 'data_stark.json'
                clave_ordenamiento = 'peso'
                heroes_desc_peso = ordenar_heroes_descendente_csv_json(archivo_json, clave_ordenamiento)

                # Imprime la lista ordenada
                if heroes_desc_peso:
                    print(f"\nLista ordenada por {clave_ordenamiento} (DESC):")
                    for item in heroes_desc_peso['lista_personajes']:
                        print(item)
                else:
                    print("Error al procesar el archivo JSON.")

            elif opcion == 6:
                #opción 6: Ordenar Lista por fuerza (Se le tiene que preguntar al usuario si ordenar de manera ASC o DESC
                heroes_ord_fuerza = ordenar_heroes_usuario('data_stark.json', 'fuerza')

                # Imprime la lista ordenada
                print(f"Héroes ordenados por fuerza según la preferencia del usuario:")
                if heroes_ord_fuerza:
                    print(f"\nLista ordenada por fuerza:")
                    for item in heroes_ord_fuerza['lista_personajes']:
                        print(item)
                else:
                    print("Error al procesar lista.") 
                        
            elif opcion == 7:
                #opción 7: Salir
                print("Fin del Programa")
                break

            else:
                print("Opción no válida. Por favor, elija una opción válida.")
        else:
            print("Debe seleccionar la opción 1 (Normalizar datos)")

#NORMALIZAR DATOS################################################################################

def stark_normalizar_datos(lista_personajes:list):
    """
    Normaliza los datos de la lista de héroes en las claves específicas.
    Parámetros:
    - lista_heroes (list): La lista de personajes.
    No retorna nada.
    """
    #verifica si la entrada es una lista no vacía
    if type(lista_personajes) == list and len(lista_personajes) == 0:
        print("Error: Lista de héroes vacía")

    # Claves específicas a sanitizar
    claves_a_sanitizar = ['altura', 'peso', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia']

    for personaje in lista_personajes: #itera sobre cada personaje en la lista
        #itera sobre claves específicas que se desean normalizar
        for clave in claves_a_sanitizar:
            if clave in personaje:  #verifica si la clave está presente en el diccionario del personaje
                sanitizar_dato(personaje, clave, 'str')

    print('Datos normalizados')

def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str):
    """
    Sanitiza el valor del diccionario correspondiente a la clave y tipo de dato especificados.
    Parámetros:
    - heroe (dict): El diccionario con los datos del personaje.
    - clave (str): La clave del diccionario que se desea sanitizar.
    - tipo_dato (str): El tipo de dato a sanitizar ('string', 'entero' o 'flotante').
    Retorna:
    bool: True si se ha sanitizado algún dato, False en caso contrario.
    """
    tipo_dato = tipo_dato.lower() #convierte el tipo de dato a minúsculas para facilitar la comparación
     #verifica si el tipo de dato es reconocido (str, int, o float)
    if tipo_dato not in ['str', 'int', 'float']:
        print('Tipo de dato no reconocido')
        return False
    #verifica si el valor asociado con la clave en el diccionario es del tipo especificado
    if clave not in heroe:
        print("La clave especificada no existe en el héroe")
        return False
    #realiza la conversión y sanitización según el tipo de dato especificado
    if tipo_dato == str:
        heroe[clave] = sanitizar_string(heroe[clave]) #llama a la función sanitizar_string para cadenas
    elif tipo_dato == int:
        heroe[clave] = sanitizar_entero(heroe[clave]) #llama a la función sanitizar_entero para enteros
    elif tipo_dato == float:
        heroe[clave] = sanitizar_flotante(heroe[clave]) #llama a la función sanitizar_entero para flotantes

    return True #retorna True si la sanitización fue exitosa

def sanitizar_entero(numero_str:str):
    '''
    Realiza diferentes comprobaciones y convierte el string en el 
    tipo de número correspondiente.
    Parámetros:
    numero_str (str): Un string que representa un posible número entero o flotante.
    Retorna:
    int or float or -1 or -2 or -3: Dependiendo del análisis del string
    '''
    #elimina cualquier espacio en blanco al principio y al final de una cadena
    numero_str = numero_str.strip()
    
    if not numero_str: #verifica si la cadena está vacía después de quitar los espacios en blanco
        return -3 #retorna -3 si la cadena está vacía
    
    #verifica si el primer carácter es un signo menos
    if numero_str and numero_str[0] == '-':
        #si el primer carácter es un signo menos, verifica si los caracteres restantes son todos dígitos
        if numero_str[1:].isdigit():
            return -2 #retorna -2 si es un número entero negativo
        else:
            return -1 #retorna -1 si hay caracteres no numéricos después del signo menos

    try:
        numero = int(numero_str) #intenta convertir la cadena a un número entero
        return numero #retorna el número entero si la conversión es exitosa
    except ValueError:
        try:
            if float(numero_str): #intenta convertir la cadena a un número flotante
                return -3 #retorna -2 si es un número flotante negativo
        except ValueError:
            return -1 #retorna -1 si hay un error en la conversión a entero o flotante

def sanitizar_flotante(numero_str:str):
    """
    Analiza un string para determinar si es un número flotante positivo.
    Parámetros:
    - numero_str (str): El string que representa un posible número flotante.
    Retorna:
    float: El número flotante positivo si es válido.
           -1 si contiene caracteres no numéricos.
           -2 si el número es negativo.
           -3 si ocurren otros errores que no permiten convertirlo a flotante.
    """
    try:
        #elimina espacios en blanco al principio y al final
        numero_str = numero_str.strip()

        #verifica si contiene caracteres no numéricos
        # verifica si la cadena original numero_str (después de eliminar los puntos) contiene caracteres que no son dígitos
        if not numero_str.replace('.', '').isdigit():
            return -1

        #convierte a flotante y verifica si es negativo
        numero_float = float(numero_str)
        if numero_float < 0:
            return -2

        return numero_float

    except ValueError:
        return -3

def sanitizar_string(valor_str:str, valor_por_defecto=''):
    """
    Analiza un string y realiza acciones según las condiciones especificadas.

    Parámetros:
    - valor_str (str): El string que se debe analizar.
    - valor_por_defecto (str, opcional): El valor por defecto a retornar si el string está vacío.

    Retorna:
    str: El string resultante después de las acciones de análisis y transformación.
    """
    #elimina espacios en blanco al principio y al final de los parámetros
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()

    #reemplaza '/' por un espacio
    valor_str = valor_str.replace('/', ' ')

    #verifica si 'valor_str' contiene solo texto sin números
    if valor_str and not valor_str.isalpha():
        return "N/A" #no aplicable, no disponible
   #retorna el valor por defecto convertido a minúsculas si 'valor_str' está vacío
    elif not valor_str and valor_por_defecto:
        return valor_por_defecto.lower()
    else:
        return valor_str.lower()