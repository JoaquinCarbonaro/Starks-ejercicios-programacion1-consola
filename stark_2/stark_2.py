'''
nombre: Joaquin
apellido: Carbonaro

Desafío #02:
Usando como base lo realizado en el anterior desafío realizar los siguientes
informes en un menú
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia
NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú
'''

from data_stark import lista_personajes
from funciones import *

lista_superheroes_filtrados_genero = []
lista_personaje_f_altura = []
lista_personaje_m_altura = []
lista_personaje_m_fuerza = []
lista_personaje_nb_fuerza = []
dic_ojos_contar = {}
dic_pelo_contar = {}
dic_ojos_agrupar = {}
dic_inteligencia_agrupar = {}

normalizar_datos(lista_personajes)

while True: 
    opcion = mostrar_menu()

    if opcion == "A":
        lista_superheroes_filtrados_genero = buscar_superheroes_genero(lista_personajes,"NB")
        imprimir_superheroes_nb(lista_superheroes_filtrados_genero)

    elif opcion == "B":
        lista_superheroes_filtrados_genero = buscar_superheroes_genero(lista_personajes,"F")
        lista_personaje_f_altura = encontrar_maximo_minimo(lista_superheroes_filtrados_genero, "altura", "maximo")
        imprimir_superheroe_maximo_minimo(lista_personaje_f_altura, "F", "altura")

    elif opcion == "C":
        lista_superheroes_filtrados_genero = buscar_superheroes_genero(lista_personajes,"M")
        lista_personaje_m_altura = encontrar_maximo_minimo(lista_superheroes_filtrados_genero, "altura", "maximo")
        imprimir_superheroe_maximo_minimo(lista_personaje_m_altura, "M", "altura")

    elif opcion == "D":
        lista_superheroes_filtrados_genero = buscar_superheroes_genero(lista_personajes,"M")
        lista_personaje_m_fuerza = encontrar_maximo_minimo(lista_superheroes_filtrados_genero, "fuerza", "minimo")
        imprimir_superheroe_maximo_minimo(lista_personaje_m_fuerza, "M", "fuerza")

    elif opcion == "E":
        lista_superheroes_filtrados_genero = buscar_superheroes_genero(lista_personajes,"NB")
        lista_personaje_nb_fuerza = encontrar_maximo_minimo(lista_superheroes_filtrados_genero, "fuerza", "minimo")
        imprimir_superheroe_maximo_minimo(lista_personaje_nb_fuerza, "NB", "fuerza")

    elif opcion == "F":
        lista_superheroes_filtrados_genero = buscar_superheroes_genero(lista_personajes,"NB")
        promedio = calcular_fuerza_promedio(lista_superheroes_filtrados_genero)
        imprimir_fuerza_promedio(promedio)

    elif opcion == "G":
        dic_ojos_contar = contar_agrupar_caracteristica(lista_personajes, "color_ojos", "contar")
        imprimir_contar_agrupar_caracteristica(dic_ojos_contar, "color_ojos")

    elif opcion == "H":
        dic_pelo_contar = contar_agrupar_caracteristica(lista_personajes, "color_pelo", "contar")
        imprimir_contar_agrupar_caracteristica(dic_pelo_contar, "color_pelo")

    elif opcion == "I":
        dic_ojos_agrupar = contar_agrupar_caracteristica(lista_personajes, "color_ojos", "agrupar")
        imprimir_contar_agrupar_caracteristica(dic_ojos_agrupar, "color_ojos")

    elif opcion == "J":
        dic_inteligencia_agrupar = contar_agrupar_caracteristica(lista_personajes, "inteligencia", "agrupar")
        imprimir_contar_agrupar_caracteristica(dic_inteligencia_agrupar, "inteligencia")

    elif opcion == "S":
        print("Saliendo del programa. Hasta luego.")
        break
    
    else:
        print("Opción no válida. Por favor, elija una opción válida.")