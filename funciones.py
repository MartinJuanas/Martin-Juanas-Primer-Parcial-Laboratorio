import csv
import re
from functools import reduce

def validar_espacios(cadena: str) -> bool:
    """esta funcion valida que un input no tenga espacios al final ni al comienzo del mismo.

    Args:
        cadena (str): str que se evalua con el metodo "strip"

    Returns:
        bool: devuelve un boleano
    """
    if cadena.strip() == cadena:
        return True
    else:
        return False


def crear_lista(mensaje:str) -> list:
    """Genera una lista apartir de lo que ingrese el usuario.

    Args:
        mensaje (str): Mensaje que se quiere mostrar por consola

    Returns:
        list: devuelve una lista con los datos ingresados por el usuario.
    """
    lista = []

    while True:
        elemento = input(mensaje)

        if validar_espacios(elemento):
            lista.append(elemento)
        else:
            print("¡ Error ! No se permiten espacios al pricipio y al final de la frase.")

        respuesta = input("Quiere seguir agregando cosas a la lista ?(si/no): ")
        if respuesta == "no":
            break

    return lista

def ordenar_lista(lista, orden, clave, clave2):
    bandera_swap = True
    while bandera_swap:
        bandera_swap = False
        for i in range(len(lista)-1):
            if (lista[i][clave] < lista[i+1][clave] and orden == "ascendente") or (lista[i][clave] > lista[i+1][clave] and orden == "descendente"):
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                bandera_swap = True
            if lista[i][clave] == lista[i+1][clave]:
                if lista[i][clave2] > lista[i+1][clave2]: 
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera_swap = True


def mostrar(lista):
    """Esta funcion recibe una lista y a muestra con cierto "formato"

    Args:
        lista (_type_): lista sobre la que se itera y se sacan los datos a mostrar
    """
    print("|id|  Marca  |             Objeto           | Precio  |")
    for elemento in lista:
        print(f"|{elemento['id']:<1}|{elemento['Marca']:<30}|{elemento['Objeto']:<45} |{elemento['Precio']:<60}|")



def mostrar_menu() -> str:
    """muestra menu opciones 
    Returns:
        str: opcion ingresada por usuario.
    """
    print("""   
    Menú:
    1. Cargar lista de insumos desde archivo CSV.
    2. Listar cantidad por marca.
    3. Listar insumos por marca.
    4. Buscar insumo por característica.
    5. Listar insumos ordenados.
    6. Realizar compras.
    7. Guardar Json con productos que contengan "Disco Duro" en el nombre.
    8. Mostrar lo guardado en el Archivo Json.
    9. Actualizar precios.
    10. Salir
    """)

    opcion = input("Ingrese opcion: ")
    return opcion

def validar_input_numerico(user_num:str,min:int,max:int)->int:
    """Valida un input numerico ingresado por el usuario.

    Args:
        user_num (str): Ingreso del dato del usuario
        min (int): rango minimo para validar
        max (int): rango maximo para validar

    Returns:
        int: Devuelve el dato validado
    """
    while True:
            try:
                numero_validado = int(user_num)
                while numero_validado<min or numero_validado>max: #Validacion en un rango
                    numero_validado=int(input("Error, ingreso fuera del rango,reintentar: "))
                break
            except:
                print("No es un valor valido.")
                user_num = input("Ingrese un valor numerico : ")
        

    return numero_validado


def validar_entrada_str(mensaje:str)->str:
    """Valida que una entrada sea solo en minuscula y que no sea un str ni otra cosa.

    Args:
        mensaje (str): input del usuario

    Returns:
        str: input del usuario validado
    """
    while True:
        entrada = input(mensaje)
        entrada = entrada.lower()
        if entrada.isdigit():
            print("Entrada inválida. Debes ingresar texto, no números.")
        elif entrada == "no":
            break
        elif entrada != "si":
            print("Entrada inválida. Debes ingresar 'si' o 'no'.")
        else:
            return entrada