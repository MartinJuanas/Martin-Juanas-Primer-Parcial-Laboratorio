from funciones import *
def obtener_caracteristicas(lista: list, caracteristica) -> list:
    """Esta funcion genera una lista de "caracteristicas" en base a la key que se le pase en el parametro caracteristicas.
        las mismas no se repiten debido a que se utiliza un set y luego el mismo se lo pasa a lista con la propia funcion list.

    Args:
        lista (list): Recibe una lista a iterar 
        caracteristica (str): Caracteristica por la cual se desea filtrar la lista pasada

    Returns:
        list: devuelve una lista con las caracteristicas filtradas
    """
    lista_filtrada = list(set(map(lambda e: e[caracteristica], lista)))
    return lista_filtrada


def contar_por_caracteristica(lista_filtrada: list, key_caracteristica: str, lista_sin_filtrar: list):
    """cuenta los elementos que hay en una lista que cumplan con la igualdad de lo que le pasemos en key
        caracteristica.

    Args:
        lista_filtrada (list):lista con los elementos que se desean buscar y comparar
        key_caracteristica (str): Es la clave con la que se compara la "lista filtrada"
        key_nombre (str): Clave que representa el nombre de lo que analizamos (nombres,marcas,caracteristicas,etc)
        lista_sin_filtrar (list): lista con los elementos sin filtrar.
    """
    for i in lista_filtrada:
        print("-----------------------------------------------------")
        print(f"{i}")
        print("-----------------------------------------------------")
        contador_cada_caracteristica = 0
        for elemento in lista_sin_filtrar:
            if elemento[key_caracteristica] == i:
                contador_cada_caracteristica += 1
        print(f"Total de productos: {contador_cada_caracteristica}")


def mostrar_por_caracteristicas(lista_filtrada: list, key_caracteristica: str, key_caracteristica2, key_caracteristica3, lista_sin_filtrar: list):
    """_summary_

    Args:
        lista_filtrada (list): lista con los elementos que se desean buscar y comparar
        key_caracteristica (str): Es la clave con la que se compara la "lista filtrada"
        key_caracteristica2 (_type_): dato que se quiera mostrar
        key_caracteristica3 (_type_): otro dato que se quiera mostrar
        lista_sin_filtrar (list): lista con los elementos sin filtrar
    """
    for i in lista_filtrada:
        print("-----------------------------------------------------")
        print(f"{i}")
        print("-----------------------------------------------------")
        for elemento in lista_sin_filtrar:
            if elemento[key_caracteristica] == i:
                print(elemento[key_caracteristica2],
                      elemento[key_caracteristica3])


def filtrar_por_caracteristica(lista_caracteristicas: list, lista_insumos: list, key: str,) -> list:

    """Crea una lista nueva en base a la key que se le pase. 

    Args:
        lista_caracteristicas (list): lista de caracteristicas a comparar
        lista_insumos (list): lista sin filtrar
        key (str): Key que se quiere analizar

    Returns:
        list: devuelve una lista que contiene aquellos elementos que posean la misma key que se analizo
    """
    lista_resultados = []
    for insumo in lista_insumos:
        resultados = list(
            filter(lambda a: insumo in a[key], lista_caracteristicas))
        lista_resultados.extend(resultados)
    return  lista_resultados

def actualizar_precio_cantidad(lista:list,rango_minimo:int,rango_maximo:int,key:str)->list:
    """Actualiza una key numerica de precio/cantidad por un valor ingresado por el usuario

    Args:
        lista (list): lista
        rango_minimo (int): rango de validacion numerica minimo
        rango_maximo (int): rango de validacion numerica maximo
        key (str): key a actualizar el valor

    Returns:
        list: devuelve una lista con los valores actualizados
    """
    lista_nueva =[]
    for i in  lista :
        cantidad = input(f"Ingrese la cantidad de unidades de '{i[key]}' que desea agregar al carrito: ")
        cantidad_validada=validar_input_numerico(cantidad,rango_minimo,rango_maximo)
        i["Cantidad"] = cantidad_validada
        i["Precio"] *= cantidad_validada
        lista_nueva.append(i)
    return lista_nueva

def acumular_key_numerica(lista: list, key: str) -> int:
    """Acumulador de los valores de una key numerica dentro de la lista,itera sobre la misma y suma el valor dentro de la key 

    Args:
        lista (list): lista a iterar sobre la cual se quiere acumular
        key (str): key a acumular

    Returns:
        int: devuelve un entero resultado de la acumulacion de valores en la key
    """

    precio_total = 0
    for i in range(len(lista)):
        precio_total += lista[i][key]
    return precio_total

def actualizar_key_numerica(lista:list,aumento:float,key:str):
    """Esta funcion aplica un aumento sobre una key numerica

    Args:
        lista (list): lista sobre la ques se itera y se aplica el aumento en la key
        aumento (float): valor ingresado por usuario
        key (str): key numerica a la cual se le quiere aplicar el aumento
    """
    for i in lista:
        i[key] *= aumento
    
    

def agregar_producto(lista:list)->dict:
    """Genera una serie de inputs al usuario para el agregado de un diccionario de un producto.

    Args:
        lista (list): lista sobre la ques se itera y se le muestra al usuario sus elementos.
    Returns:
        dict: Retorna un diccionario con los inputs del usuario.
    """
    nuevo_producto = {}
    
    numero_id = input("Ingrese número de ID del producto (50 en adelante): ")
    nuevo_producto["id"] = validar_input_numerico(numero_id, 50, 1000)
    
    nuevo_objeto = input("Ingrese nombre de objeto (Sin números): ")
    nuevo_producto["Objeto"] = nuevo_objeto
    mostrar_lista(lista)
    nueva_marca = input("Seleccione una de las marcas de la lista: ")
    nuevo_producto["Marca"] = nueva_marca
    
    nuevo_precio = input("¿Cuál es el precio del producto? (Solo valores enteros): ")
    nuevo_producto["Precio"] = validar_input_numerico(nuevo_precio,0,100000)
    
    nuevo_producto_caracteristicas = []
    while len(nuevo_producto_caracteristicas) < 3:
        caracteristica = input("Ingrese una característica del producto (Ingresar 'Salir' para finalizar. Máximo 3 características): ").capitalize
        if caracteristica == 'Salir':
            break
        nuevo_producto_caracteristicas.append(caracteristica)
    
    nuevo_producto["Caracteristicas"] = nuevo_producto_caracteristicas

    return nuevo_producto