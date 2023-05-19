import re
import json

def parser_csv(nombre_archivo: str, keys: list, patron: str) -> list:
    """Abre un archivo y genera una lista de diccionarios con los parametros pasados, filtra la lista por el patron.


    Args:
        nombre_archivo (str): direccion de archivo a abrir, o nombre en caso de estar en la misma carpeta
        keys (list): Claves a asignar a los valores dentro del diccionario que creamos para los elementos(Necesario 5 claves)
        patron (str): caracteres que querramos sacar con el metodo RE

    Returns:
        list: Devueve una lista de diccionarios con las claves asignadas en el parametro key y 
        los valores de esas key son cada elemento dentro de la lista generados por el metodo "split"
    """
    lista = []
    with open(nombre_archivo, "r", encoding='utf-8') as file:
        for linea in file:
            linea = re.sub(patron, "", linea)
            p = linea.split(",")
            elem_dict = {}
            elem_dict[keys[0]] = int(p[0])
            elem_dict[keys[1]] = (p[1])
            elem_dict[keys[2]] = (p[2])
            elem_dict[keys[3]] = float(p[3])
            elem_dict[keys[4]] = p[4].split("||")
            lista.append(elem_dict)
    return lista


def cargar_json(lista:list, nombre_archivo:str):
    """carga una lista como un archivo json

    Args:
        lista (list): lista que se desea cargar
        nombre_archivo : path donde se quiere ubicar el archivo cargado
    """
    with open(nombre_archivo, "w") as json_file:
        # Escribir la lista de diccionarios en el archivo JSON
        json.dump(lista, json_file,indent=4)
    print(f"Los datos se han guardado en el archivo JSON: {nombre_archivo}")


def cargar_txt(lista: list, nombre_archivo: str,total:int):
    """carga un archivo en formato TXT

    Args:
        lista (list): lista que se desea cargar
        nombre_archivo (str): path donde se quiere ubicar el archivo
        total (int): Total a pagar 
    """
    with open(nombre_archivo, "w") as archivo:
        for elemento in lista:
            archivo.write(str(elemento) + "\n")
            archivo.write (f"Total a pagar :${total}")
    print(f"Elementos cargados en {nombre_archivo}!")


def guardar_csv(lista: list, nombre_archivo: str):
    """guarda una lista en formato csv iterando sobrel los elementos de la lista y dandoles el formato deseado

    Args:
        lista (list): lista a iterar y guardar
        nombre_archivo (str): path de donde se quiere ubicar el archivo.
    """
    with open(nombre_archivo, "w", encoding='utf-8') as archivo:
        for elemento in lista:
            linea = f"{elemento['id']},{elemento['Objeto']},{elemento['Marca']},${elemento['Precio']:5.2f},{ '|!*|'.join(elemento['Caracteristicas'])}\n"
            archivo.write(linea)
    print(f"Archivo cargado en {nombre_archivo}")



def abrir_txt(nombre_archivo:str)->list:
    """genera una lista con los elementos dentro del archivo TXT

    Args:
        nombre_archivo (str): Ruta de acceso al TXT

    Returns:
        list: lista con los contenidos del TXT como elementos
    """
    lista =[]
    with open (nombre_archivo , "r") as archivo:
        for linea in archivo:
            linea.strip()
            lista.append(linea)
    return lista