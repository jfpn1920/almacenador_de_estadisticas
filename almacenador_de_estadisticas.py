import random
ids = []
nombres = []
valores = []
categorias = []
fechas = []
estados = []
observaciones = []
#------------------------------------------------#
#--|menu_principal_almacenador_de_estadísticas|--#
#------------------------------------------------#
while True:
    print("menu principal almacenador de estadísticas")
    print("1) crear estadística")
    print("2) editar estadística")
    print("3) eliminar estadística")
    print("4) buscar estadística")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------------#
    #--|crear_estadistica|--#
    #-----------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_estadistica = 1
        else:
            id_estadistica = ids[-1] + 1
        nombre = input("nombre de la estadística: ")
        valor = float(input("valor de la estadística: "))
        categoria = input("categoría: ")
        fecha = input("fecha de registro: ")
        estado = input("estado (activa o inactiva): ")
        observacion = input("observación: ")
        ids.append(id_estadistica)
        nombres.append(nombre)
        valores.append(valor)
        categorias.append(categoria)
        fechas.append(fecha)
        estados.append(estado)
        observaciones.append(observacion)
        print("estadística registrada correctamente.")
        print("id:", id_estadistica)
    #------------------------#
    #--|editar_estadistica|--#
    #------------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar estadística")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {valores[i]} | {categorias[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {valores[posicion]} | {categorias[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                nombres[posicion] = input("nuevo nombre de la estadística: ")
                valores[posicion] = float(input("nuevo valor de la estadística: "))
                categorias[posicion] = input("nueva categoría: ")
                fechas[posicion] = input("nueva fecha de registro: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #--------------------------#
    #--|eliminar_estadistica|--#
    #--------------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar estadística")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {valores[i]} | {categorias[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {valores[posicion]} | {categorias[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    valores.pop(posicion)
                    categorias.pop(posicion)
                    fechas.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #------------------------#
    #--|buscar_estadistica|--#
    #------------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar estadística")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {valores[posicion]} | {categorias[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            activas = 0
            inactivas = 0
            suma = 0
            mayor = valores[0]
            menor = valores[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {valores[i]} | {categorias[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
                suma += valores[i]
                if valores[i] > mayor:
                    mayor = valores[i]
                if valores[i] < menor:
                    menor = valores[i]
                if estados[i].lower() == "activa":
                    activas += 1
                elif estados[i].lower() == "inactiva":
                    inactivas += 1
            promedio = suma / len(ids)
            print("estadísticas almacenador de estadísticas")
            print("cantidad de estadísticas:", len(ids))
            print("estadísticas activas:", activas)
            print("estadísticas inactivas:", inactivas)
            print("suma de valores:", round(suma, 2))
            print("promedio de valores:", round(promedio, 2))
            print("mayor valor registrado:", round(mayor, 2))
            print("menor valor registrado:", round(menor, 2))
            posicion = random.randint(0, len(ids) - 1)
            print("simulación de almacenamiento de estadística")
            print("estadística almacenada:")
            print(f"{ids[posicion]} | {nombres[posicion]} | {valores[posicion]} | {categorias[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el almacenador de estadísticas.")
        break
    else:
        print("opción no válida.")