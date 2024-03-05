from data_stark import lista_personajes
import re

#1.1.#######################################################################################################################

def extraer_iniciales(nombre: str):
    """
    Extrae las iniciales del nombre del personaje y las formatea como iniciales seguidas de un punto.
    Parámetros:
    - nombre_heroe (str): El nombre del personaje del cual se extraerán las iniciales.
    Retorna:
    str: Las iniciales del nombre del personaje seguidas de un punto, o 'N/A' si el nombre está vacío.
    """   
    try:
        if not nombre:
            return 'N/A'

        #reemplaza el guión con un espacio en blanco si existe
        nombre = nombre.replace('-', ' ')

        #encuentra las iniciales del nombre del personaje
        palabras = nombre.split() #Divide el nombre completo en una lista con dos elementos
        iniciales = [palabra[0] for palabra in palabras if palabra.lower() != 'the']
        #estás iterando sobre cada palabra en la lista palabras.
        # filtra las palabras que no son iguales a 'the'
        #.lower() convierte la palabra a minúsculas antes de realizar la comparación
        #palabra[0] obtiene el primer carácter de cada palabra.
        #Todo esto se coloca dentro de corchetes [], creando así una lista de las iniciales de las palabras que cumplen con la condición dada.
        if iniciales:
            return '.'.join(iniciales).upper() + '.'
        else:
            return 'N/A'  #indica que la información no es aplicable o no está disponible en ese momento.

    except ValueError:
        return 'N/A'

#1.2.#######################################################################################################################

def obtener_dato_formato(dato:str):
    """
    Convierte un dato en minúsculas y lo formatea como snake_case.
    Parámetros:
    - dato (str): El dato a formatear.
    Retorna:
    str: El dato en minúsculas y con formato snake_case, o False si el dato no es un string.
    """
    if not isinstance(dato, str):
        return False

    dato = dato.lower()  #converte a minúsculas
    dato = dato.replace(' ', '_')  #reemplaza espacios por guiones bajos
    dato = re.sub(r'[^a-zA-Z0-9_]', '', dato)  #elimina caracteres especiales excepto guiones bajos
    #busca todos los caracteres que no son letras (mayúsculas o minúsculas), 
    #números o guiones bajos. ^ indica una negación, selecciona todo lo que no está en el conjunto.
    return dato

#1.3#######################################################################################################################

def stark_imprimir_nombre_con_iniciales(nombre:dict):
    """
    Imprime el nombre del personaje con asteriscos y sus iniciales entre paréntesis.
    Parámetros:
    - nombre_heroe (str): El nombre del personaje en formato snake_case.
    Retorna:
    bool: True si la impresión se realizó con éxito, False en caso de error.
    """
    #verifica si 'nombre' no es un diccionario o si está vacío
    if not isinstance(nombre, dict) and len(nombre) == 0:
        return False #retorna False si no cumple con las condiciones
     #verifica si el diccionario no contiene la clave 'nombre'
    if 'nombre' not in nombre:
        return False #retorna False si 'nombre' no está presente
    
    #obtiene el valor asociado con la clave 'nombre' del diccionario
    nombre_personaje = nombre['nombre']
    #llama a la función para obtener el formato específico del nombre del personaje
    nombre_formateado = obtener_dato_formato(nombre_personaje)
    # Llama a la función para obtener las iniciales del nombre del personaje
    iniciales = extraer_iniciales(nombre_personaje)
    #verifica si las iniciales son 'N/A'
    if iniciales == 'N/A':
        return False #retorna False si las iniciales son 'N/A'
    
    #imprime el nombre formateado con iniciales en un formato específico
    print(f"* {nombre_formateado} ({iniciales})")
    return True #retorna True para indicar que la operación fue exitosa

#1.4.#######################################################################################################################

def stark_imprimir_nombres_con_iniciales(lista_recibida: list) -> bool:
    """
    Imprime la lista de nombres de personajes con asteriscos y sus iniciales entre paréntesis.
    Parámetros:
    - lista_heroes (list): La lista de personajes (cada personaje como un diccionario).
    Retorna:
    bool: True si la impresión se realizó con éxito, False en caso de error.
    """
    #valida si lista_heroes es del tipo lista y contiene al menos un elemento
    if not isinstance(lista_recibida, list) or len(lista_recibida) == 0:
        return False

    #imprime cada nombre con iniciales utilizando stark_imprimir_nombre_con_iniciales
    for heroe in lista_recibida:
        resultado = stark_imprimir_nombre_con_iniciales(heroe)
        if not resultado:
            #si hay un error al imprimir un nombre, retorna False
            return False

    #si se imprimen todos los nombres con éxito, retorna True
    return True

#2.1.#######################################################################################################################

def generar_codigo_heroe(lista_recibida:dict, id:int):
    """
    Genera un código para un héroe en función de su género y un identificador.
    Parámetros:
    - heroe (dict): El diccionario que representa al héroe.
    - id (int): El identificador para el héroe.
    Retorna:
    str: El código generado, o 'N/A' en caso de no cumplir las validaciones.
    """
    #verifica si la lista recibida es un diccionario y contiene la clave "genero"
    if not isinstance(lista_recibida, dict) or "genero" not in lista_recibida:
        return "N/A"
    #verifica si el género es válido
    genero = lista_recibida["genero"]
    if genero != 'M' and genero != 'F' and genero != 'NB':
        return "N/A"
    
    # Determinar el primer número del código según el género
    if genero == 'M':
        primer_numero = '1'
    elif genero == 'F':
        primer_numero = '2'
    else:
        primer_numero = '0'

    #verifica si el identificador es un número entero no negativo
    if not isinstance(id, int) or id < 0:
        return "N/A"
    
    if genero == 'NB':
        id_str = str(id).zfill(6)  #rellena con ceros a la izquierda para que tenga 7 dígitos
    else:
        id_str = str(id).zfill(7)

    return f"{genero}-{primer_numero.zfill(1)}{id_str}" #retorna el código único del héroe en el formato "GÉNERO-ID"

#2.2.#######################################################################################################################

def stark_generar_codigos_heroes(lista_personajes:list):
    """
    Genera códigos para los héroes en función de su género y posición en la lista.
    Parámetros:
    - lista_heroes (list): La lista de personajes (cada personaje como un diccionario).
    Retorna:
    str: La cadena generada con los códigos, o False en caso de error.
    """
    #Verifica si lista_personajes no es una lista, está vacía o no contiene solo diccionarios
    if not isinstance(lista_personajes, list) or len(lista_personajes) == 0 or not all(isinstance(personaje, dict) for personaje in lista_personajes):
        return False

    codigos_heroes = [] #lista para almacenar los códigos generados
    #itera sobre los índices de la lista de personajes
    for i in range(len(lista_personajes)):
        #genera un código para el héroe usando la función generar_codigo_heroe
        codigo = generar_codigo_heroe(lista_personajes[i], i + 1)
        if codigo == 'N/A': #verifica si el código generado es 'N/A'
            return False #retorna False si hay un error en la generación del código
        codigos_heroes.append(codigo) #agrega el código generado a la lista de códigos

    resultados = [] #lista para almacenar los resultados finales
    #itera sobre los índices de la lista de personajes nuevamente
    for i in range(len(lista_personajes)):
        #obtiene el nombre del personaje o usa 'Nombre Desconocido' si no hay nombre
        nombre_personaje = lista_personajes[i].get('nombre')
        iniciales = extraer_iniciales(nombre_personaje) #llama a lafunción para obtener las iniciales del nombre del personaje
        #crea una cadena con el nombre formateado, iniciales y código del héroe
        resultados.append(f"* {nombre_personaje} ({iniciales}) | {codigos_heroes[i]}")
    
    codigo_final = "\n".join(resultados) #une las cadenas de resultados con saltos de línea
    #agrega información sobre la cantidad de códigos generados
    cantidad_codigos = len(resultados)
    codigo_final += f"\nCadena generada, Se asignaron {cantidad_codigos} códigos"

    return codigo_final  #retorna la cadena de códigos generada

#3.1.#######################################################################################################################

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

#3.2.#######################################################################################################################

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

#3.3.#######################################################################################################################

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

#3.4.#######################################################################################################################

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

#3.5.#######################################################################################################################

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


#4.1.#######################################################################################################################

def stark_imprimir_indice_nombre(lista_personajes:list):
    """
    Imprime las palabras de los nombres de los personajes separadas por guiones y omite la palabra "the".
    Parámetros:
    - lista_heroes (list): La lista de personajes.
    No retorna nada.
    """
    if type(lista_personajes) == list and len(lista_personajes) == 0:
        return None

    for personaje in lista_personajes:
        nombre_heroe = personaje.get('nombre', '') #obtiene el nombre del personaje o una cadena vacía si la clave 'nombre' no está presente
        nombre_limpio = nombre_heroe.replace('the', '').replace('-', ' ') #elimina las palabras 'the' y reemplaza los guiones con espacios en el nombre
        #convierte el nombre limpio en una lista de palabras, las une con guiones y las imprime
        nombre_separado = '-'.join(nombre_limpio.split())  #une el nombre con el apellido del mismo personaje
        print(nombre_separado, end='-') #une un personaje con otro


#5.1#######################################################################################################################

def generar_separador(patron: str, largo: int, imprimir: bool = True):
    """
    Genera un separador utilizando el patrón especificado y la longitud dada.
    Parámetros:
    - patron (str): Un carácter que se utilizará como patrón para generar el separador.
    - largo (int): La cantidad de caracteres que ocupará el separador.
    - imprimir (bool, opcional): Determina si se debe imprimir el separador por pantalla. Por defecto, es True.
    Retorna:
    - str: El separador generado.
    Si no se cumplen las validaciones, retorna 'N/A'.
    """
    #asegura que el patrón tenga una longitud válida y que el largo esté en el rango permitido
    if not (1 <= len(patron) <= 2) or not  (isinstance(largo, int) and 1 <= largo <= 235):
        return 'N/A'
    
    separador = patron * largo #genera el separador concatenando el patrón según la longitud especificada
    #verifica si se debe imprimir el separador
    if imprimir:
        #imprime el separador y luego lo retorna
        print(separador)
        return separador
    else:
        return separador

#5.2#######################################################################################################################

def generar_encabezado(titulo: str):
    """
    Genera un encabezado con el título en mayúsculas envuelto entre dos separadores.
    Parámetros:
    - titulo (str): El título de la sección.
    Retorna:
    - str: El encabezado con el título en mayúsculas envuelto entre separadores.
    """
    titulo_en_mayusculas = titulo.upper() #convierarte el título a mayúsculas
    #genera un separador utilizando la función gener_separador
    # con el patrón '*' y una longitud calculada a partir del tamaño del título
    separador = generar_separador('*', 100, False)
    #retorna el encabezado formateado con el separador y el título en mayúsculas
    return f"{separador}\n{titulo_en_mayusculas}\n{separador}"

#5.3#######################################################################################################################

def imprimir_ficha_heroe(personaje: dict):
    """
    Imprime la ficha de un héroe con el formato especificado.
    Parámetros:
    - heroe (dict): Un diccionario con los datos del héroe.
    Retorna:
    - printeo de encabezados en mayúsculas y datos envuelto entre separadores.
    """
    #genera los separadores para las secciones principales de la ficha
    separador_principal = generar_encabezado("Principal")
    separador_fisico = generar_encabezado("Fisico")
    separador_senias = generar_encabezado("Señas Particulares")
    
    #obtiene información del diccionario del héroe (o usa valores predeterminados si no están presentes)
    nombre_personaje = personaje.get('nombre', 'Nombre Desconocido')
    nombre_personaje_formato = obtener_dato_formato(nombre_personaje)
    iniciales_personaje = extraer_iniciales(nombre_personaje)
    
    identidad_secreta = personaje.get('identidad', 'Identidad Desconocida')
    identidad_secreta = obtener_dato_formato(identidad_secreta)

    consultora = personaje.get('empresa', 'Consultora Desconocida')
    consultora = obtener_dato_formato(consultora)

    codigos_heroes = [] 
    for i in range(len(lista_personajes)):
        codigo = generar_codigo_heroe(lista_personajes[i], i + 1)
        if codigo == 'N/A': 
            return False 
        codigos_heroes.append(codigo) 
    # encuentra el código correspondiente al personaje actual
    codigo_actual = codigos_heroes[lista_personajes.index(personaje)]
    
    altura = personaje.get('altura', 'Altura Desconocida')
    altura = f'{float(altura):.2f}'

    peso = personaje.get('peso', 'Peso Desconocido')
    peso = f'{float(peso):.2f}'

    fuerza = personaje.get('fuerza', 'Fuerza Desconocida')
    fuerza = f'{int(fuerza)}'

    color_ojos = personaje.get('color_ojos', 'Color de Ojos Desconocido')

    color_pelo = personaje.get('color_pelo', 'Color de Pelo Desconocido')

    #formatea la ficha con la información obtenida
    ficha_formato = f"{separador_principal}\n" \
                    f"     NOMBRE DEL HÉROE:       {nombre_personaje_formato} ({iniciales_personaje})\n" \
                    f"     IDENTIDAD SECRETA:      {identidad_secreta}\n" \
                    f"     CONSULTORA:             {consultora}\n" \
                    f"     CÓDIGO DE HÉROE :       {codigo_actual}\n" \
                    f"{separador_fisico}\n" \
                    f"     ALTURA:                 {altura} cm.\n" \
                    f"     PESO:                   {peso} kg.\n" \
                    f"     FUERZA:                 {fuerza} N\n" \
                    f"{separador_senias}\n" \
                    f"     COLOR DE OJOS:          {color_ojos}\n" \
                    f"     COLOR DE PELO:          {color_pelo}\n"
    print(ficha_formato)

#5.5.#######################################################################################################################

def stark_navegar_fichas(lista_personaje:list):
    """
    Permite navegar por las fichas de héroes en la lista.
    Parámetros:
    - lista_heroes (list): La lista de personajes.
    Nota: La función maneja la navegación de fichas de héroes y permite al usuario moverse entre ellas.
    """
    if type(lista_personaje) == list and len(lista_personaje) == 0:
        print("Error: Lista de héroes vacía")
   
    total_personajes = len(lista_personaje) #obtiene la cantidad total de personajes en la lista
    i = 0 #inicializa el índice a 0
    while True:
        imprimir_ficha_heroe(lista_personaje[i]) #imprime la ficha del héroe actual
        opcion = input("[ 1 ] Ir a la izquierda\n[ 2 ] Ir a la derecha\n[ 3 ] Salir\nIngrese su opción: ")
        #solicita la entrada del usuario para elegir la siguiente acción
        '''
        En este caso, si indice_actual es 4 y sumamos 1, obtenemos 5, pero al usar % total_elementos, 
        el resultado es 0, creando así un ciclo circular.
        '''
        if opcion == '1':  #opción '1': Ir a la izquierda
            i = (i - 1) % total_personajes
        elif opcion == '2': #opción '2': Ir a la derecha
            i = (i + 1) % total_personajes
        elif opcion == '3': #opción '3': Salir
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

#6.#######################################################################################################################

def imprimir_menu():
    '''
    Imprime el menú principal de la aplicación Stark.
    Parámetros: Ninguno
    Devuelve: los datos printeados.
    '''
    print("\nMenú de Informes:\n\
    1.Imprimir la lista de nombres junto con sus iniciales\n\
    2.Imprimir la lista de nombres y el código del mismo\n\
    3.Normalizar datos\n\
    4.Imprimir índice de nombres\n\
    5.Navegar fichas\n\
    6.Salir")

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
        if (opcion >= 1) and (opcion <= 6):
            return opcion
    return False

def stark_marvel_app(lista_personajes:list):
    '''
    Aplicación principal de Stark que interactúa con el usuario y realiza la accion solicitada.
    Parámetros: lista_personajes (lista de diccionarios).
    Devuelve: los datos printeados.
    '''
    while True:
        opcion = stark_menu_principal()

        if opcion == 1:
            stark_imprimir_nombres_con_iniciales(lista_personajes)
        elif opcion == 2:
            lista_nombres_código = stark_generar_codigos_heroes(lista_personajes)
            if lista_nombres_código:
                print(lista_nombres_código)
            else:
                print("Error al generar la lista con códigos")
        elif opcion == 3:
            stark_normalizar_datos(lista_personajes)
        elif opcion == 4:
            stark_imprimir_indice_nombre(lista_personajes)
        elif opcion == 5:
            stark_navegar_fichas(lista_personajes)
        elif opcion == 6:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")