from funciones_archivos import *
from funciones_dict import *
from funciones import *
import os
bandera_opcion1 = False
bandera_opcion6 = False

while True:
    os.system("cls")
    match(mostrar_menu()):
        case "1":
            lista_insumos = parser_csv("insumos.csv", [
                                       "id", "Objeto", "Marca", "Precio", "Caracteristicas"], r'["\'$\n*!]')
            if lista_insumos:
                bandera_opcion1 = True
                print("Lista cargada.")
                for elemento in lista_insumos:
                    print(elemento)
        case "2":
            if bandera_opcion1:
                lista_marcas = obtener_caracteristicas(lista_insumos, "Marca")
                contar_por_caracteristica(lista_marcas, "Marca", lista_insumos)
            else:
                print("Debes de seleccionar la opcion 1 primero.")
        case "3":
            if bandera_opcion1:
                lista_marcas = obtener_caracteristicas(lista_insumos, "Marca")
                mostrar_por_caracteristicas(
                    lista_marcas, "Marca", "Objeto", "Precio", lista_insumos)
            else:
                print("Debes de seleccionar la opcion 1 primero.")
        case "4":
            if bandera_opcion1:

                lista_caracteristicas = crear_lista(
                    "Ingrese las caracteristicas por las que quiera filtrar: ")

                lista_filtrada = filtrar_por_caracteristica(
                    lista_insumos, lista_caracteristicas, "Caracteristicas")

                mostrar(lista_filtrada)
            else:
                print("Debes seleccionar la opcion 1 primero.")
        case "5":

            if bandera_opcion1:
                ordenar_lista(lista_insumos, "descendente", "Marca", "Precio")
                mostrar(lista_insumos)
            else:
                print("Debes de seleccionar la opcion 1 primero !")
        case "6":
            if bandera_opcion1:
                while True:
                    lista_resultados = filtrar_por_caracteristica(lista_insumos, crear_lista(
                        "Ingrese la marca de los productos que desea buscar: "), "Marca")
                    mostrar(lista_resultados)
                    lista_carrito = filtrar_por_caracteristica(
                        lista_resultados, crear_lista("ingrese el producto que desee: "), "Objeto")
                    mostrar(lista_carrito)
                    p = actualizar_precio_cantidad(
                        lista_carrito, 1, 100, "Objeto")
                    precio_final = acumular_key_numerica(p, "Precio")

                    repuesta = validar_entrada_str(
                        f"¿Desea confirmar la compra? El precio total es de {precio_final:5.2f} (si/no): ")

                    if repuesta == "si":
                        cargar_txt(p, "archivo_carrito.txt", precio_final)
                        break
                    else:
                        break
            else:
                print("Primero debes de completar la opcion 1.")
        case "7":

            if bandera_opcion1:
                lista_resultados = filtrar_por_caracteristica(lista_insumos, crear_lista(
                    "Ingrese el nombre del insumo que desea buscar: "), "Objeto")
                cargar_json(lista_resultados, "archivo_productos.json")
                bandera_opcion6 = True
            else:
                print("Debes de seleccionar la opcion 1 primero !")
        case "8":
            if bandera_opcion6:
                mostrar(lista_resultados)
            else:
                print("Primero debes de cargar la opcion 6 !")
        case "9":
            if bandera_opcion1:
                actualizar_key_numerica(
                    lista_insumos, 1.56, "Precio")
                guardar_csv(lista_insumos, "Insumos_actualizados.csv")
            else:
                print("Debes de completar la opcion 1 primero.")
        case "10":

            confirma = input("Esta seguro que desea salir ? (si/no): ")
            if (confirma == "si"):
                break
    input("Presione enter para continuar...")
