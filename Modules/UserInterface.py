from Modules.SliceAdministrator import SliceAdministrator
from Topology import *
from Modules.UserInterface import *
import json
import os
from conf.Conexion import *

class UserInterface:
    def __init__(self):
        self.Menu=None

    @staticmethod
    def main_menu():
        print('1. Configurar')
        print('2. Listar slices')
        print('3. Borrar slice')
        print('4. Definir zona de disponibilidad')
        print('5. Salir')
        return input('Opción: ')

    @staticmethod
    def def_zona_disponibilidad_menu():
        print('*********************************')
        print('Ingrese el nombre de la zona de disponibilidad:')
        return input('Nombre: ')


    @staticmethod
    def def_zona_disponibilidad_menu2():
        print('*********************************')
        print('Seleccionar:')
        print('1. Cluster de servidores Linux')
        print('2. Openstack')
        print('3. Salir')
        return input('Opción: ')

    @staticmethod
    def def_zona_disponibilidad_menu3():
        print('*********************************')
        conn = Conexion()
        server = conn.Select("recursos_id_estado,servidor,id_servidor", "servidor","-1")
        print('Lista de servidores disponibles:')
        i=0
        lista=[]
        for nombre in server:
            i=i+1
            id = conn.Select("recursos_id_estado", "servidor", f"nombre = {nombre}")
            data = conn.Select("ram,vcpu,storage", "recursos", f"id_estado = {id}")
            print(f"{i}. {nombre} - Capacidad: RAM:{data[0]}MB CPU:{data[1]} DISCO:{data[2]}")
            dic = {i: nombre}
            lista.append(dic)
        print('1. Server 1 - Capacidad: RAM:8GB  CPU:12 DISCO:10GB ')
        #print('2. Server 2 - Capacidad: RAM:8GB  CPU:12 DISCO:10GB')
        print("Escriba 'exit' si terminó de escoger los servidores para su zona de disponibilidad")
        return input('Opción: '),lista

    @staticmethod
    def def_listar_menu1():
        print('*********************************')
        print('Seleccione una zona de disponibilidad:')
        print('Lista de zonas de disponibilidad:')
        print('1. Zona 1')
        print('2. Zona 2')
        print('3. Zona 3')
        print('4. Zona 4')
        print('5. Zona 5')
        print("Escriba 'exit' para salir del menú")
        return input('Opción: ')

    @staticmethod
    def def_listar_menu2():
        print('*********************************')
        print('Seleccione un slice si desea verlo con mayor detalle:')
        print('Lista de slices:')
        print('1. Slice 1')
        print('2. Slice 2')
        print('3. Slice 3')
        print('4. Slice 4')
        print('5. Slice 5')
        print("Escriba 'exit' para salir del menú")
        return input('Opción: ')

    @staticmethod
    def def_borrar_menu3(nombre):
        print('*********************************')
        print('¿Está seguro que desea borrar el slice?', nombre)
        print('1. SI')
        print('2. NO')
        return input('Opción: ')



    @staticmethod
    def def_borrar_menu1():
        print('*********************************')
        print('Seleccione una zona de disponibilidad:')
        print('Lista de zonas de disponibilidad:')
        print('1. Zona 1')
        print('2. Zona 2')
        print('3. Zona 3')
        print('4. Zona 4')
        print('5. Zona 5')
        print("Escriba 'exit' para salir del menú")
        return input('Opción: ')

    @staticmethod
    def def_borrar_menu2():
        print('*********************************')
        print('Seleccione el slice que desea borrar:')
        print('Lista de slices:')
        print('1. Slice 1')
        print('2. Slice 2')
        print('3. Slice 3')
        print('4. Slice 4')
        print('5. Slice 5')
        print("Escriba 'exit' para salir del menú")
        return input('Opción: ')

    @staticmethod
    def def_conf_menu1():
        print('*********************************')
        print('Seleccionar:')
        print('1. Configuración desde cero')
        print('2. Continuar configuración:')
        print("Escriba 'exit' para salir del menú")
        return input('Opción: ')

    @staticmethod
    def def_conf_menu2():
        print('*********************************')
        print('Seleccionar:')
        print('1. Cluster de servidores Linux')
        print('2. Openstack')
        print('3. Salir')
        return input('Opción: ')

    @staticmethod
    def def_conf_menu3():
        print('*********************************')
        print('Seleccionar:')
        print('1. Cluster de servidores Linux')
        print('2. Openstack')
        print('3. Salir')
        return input('Opción: ')

    @staticmethod
    def def_conf_nodos1():
        print('*********************************')
        print('Seleccione:')
        print('1. Configurar todos los nodos')
        print('2. Configurar un nodo o una lista de nodos')
        print("Escriba 'exit' para salir del menú")
        return input('Opción: ')

    @staticmethod
    def def_conf_nodos2():
        print('*********************************')
        print('Seleccionar:')
        print('1. Configuración con flavors')
        print('2. Configuración manual')
        print("Escriba 'exit' para salir del menú")
        return input('Opción: ')

    @staticmethod
    def def_config_slice():
        print('*********************************')
        print('Seleccionar:')
        print('1. Agregar un nodo')
        print('2. Agregar conjunto de nodos(subgrafo)')
        print('3. Agregar enlace')
        print('4. Borrar nodo')
        print('5. Borrar enlace')
        print('6. Configurar Nodos')
        print('7. Guardar cambios')
        print('8. Ver slice actual')
        print("Escriba 'exit' para salir del menú")
        return input('Opción: ')

    @staticmethod
    def draw_subgrafo(slice, prox_node):
        # Metodo que recibe el slice actual (slice) y el nodo por el cual empezara el subgrafo (prox_node)
        # Devuelve el nuevo slice y valor del proximo valor nodo a utilizar
        topology = Topology()
        sub_topologies = ["lineal", "malla", "árbol", "anillo", "bus", "estrella"]
        print("Escoja la topología del subgrafo que desea agregar:")
        index = 0
        sub_grafo, last_node = None, None
        for sub_topology_name in sub_topologies:
            print(f"{index+1}. {sub_topology_name}")
            index += 1
        topo_type = input('Opción: ')
        if topo_type == "1":
            nodo = int(input("Ingrese el número de nodos: "))
            sub_grafo, last_node = topology.create_lineal_topology(prox_node, nodo)
        elif topo_type == "2":
            nodo = input("Ingrese el número de filas y columnas con el formato '3-3': ")
            formato = nodo.split("-")
            sub_grafo, last_node = topology.create_malla_topology(prox_node, int(formato[0]),int(formato[1]))
        elif topo_type == "3":
            nivel = int(input("Ingrese el número de niveles: "))
            sub_grafo, last_node = topology.create_tree_topology(prox_node, nivel)
        elif topo_type == "4":
            nodo = int(input("Ingrese el número de nodos: "))
            sub_grafo, last_node = topology.create_ring_topology(prox_node, nodo)
        elif topo_type == "5":
            #BUS
            nivel = int(input("Ingrese el número de niveles: "))
            sub_grafo, last_node = topology.create_star_topology(prox_node, nivel)
        elif topo_type == "6":
            nodo = int(input("Ingrese el número de nodos que irán alrededor del nodo principal: "))
            sub_grafo, last_node = topology.create_star_topology(prox_node, nodo)
        else:
            print("Opción no válida")
        prox_node = last_node+1
        slice["nodos"].update(sub_grafo) # Agrega los nuevos valores de sub_grafo al diccionario slice.
        print(f"* Subgrafo del tipo {sub_topologies[int(topo_type)-1]} agregado.")
        return slice, prox_node

    @staticmethod
    def save_changes(slice, from_scratch):
        if from_scratch:
            print("1. Guardar borrador")
            print("2. Implementar slice")
            print("Escriba 'exit' para salir del menú")
            opt = input("Opcion: ")
            if opt == "1" or opt == "2":
                if opt == "1":
                    f = open(f"./Modules/Slices/{slice['nombre']}.json", "w")
                    f.write(json.dumps(slice))
                    f.close()
                    print(f"* Slice {slice['nombre']} guardado.")
                elif opt == "2":
                    lista_zonas=[["zona1"," 4 discos-60%, 8GB RAM-50%, 8 CPUs-20%"],["zona2","4 discos-60%, 8GB RAM-70%, 8 CPUs-40%"],["zona3","4 discos-80%, 8GB RAM-90%, 8 CPUs-70%"]]
                    print("Seleccionar zona de disponibilidad:")
                    print("Lista de zonas:")
                    for zona in lista_zonas:
                        print(f"* {zona[0]}  Consumo usado: {zona[1]} ")
                    opt = input("Opcion: ")
                    slice["zona"] = {"nombre":opt}
                    print("**************************************")
                    print("Se está implementando...")
                    print(f"Se envía al administrador de slice: {slice}")
                    print("**************************************")
                    result = UserInterface.create_topology(slice)
        else:
            f = open(f"./Modules/Slices/{slice['nombre']}.json", "w")
            f.write(json.dumps(slice))
            f.close()
            print("* Cambios guardados e implementando slice ...")
            result = UserInterface.create_topology(slice)
            # TODO

    @staticmethod
    def validate_option(option):
        if not((option > 0) and (option < 100)):
            raise Exception('Invalid option')
        else:
            return True

    @staticmethod
    def exit():
        print('Elaborado por GRUPO 1\n')

    @staticmethod
    def iniciar_programa():
        o = UserInterface()
        while True:
            print('*********************************')
            print('')
            option = UserInterface.main_menu()
            try:
                option = int(option)
                UserInterface.validate_option(option)

                if option == 1:
                    while True:
                        config_mode = o.def_conf_menu1()
                        if config_mode=="exit":
                            break
                        elif int(config_mode) == 1 or int(config_mode) == 2:
                            slice = {"nodos":{}}
                            prox_node = 0
                            from_scratch = False #TODO: Cambiar a si esta implementado o no
                            if int(config_mode) == 1:
                                slice_name = input("Nombre del slice: ")
                                slice["nombre"] = slice_name
                                print(f"* Slice {slice_name} creado.")
                                from_scratch = True # Es verdadero si se inicia desde cero la creacion del slice
                            else:
                                files = os.listdir('./Modules/Slices')
                                i = 0
                                for file_name in files:
                                    print(f"{i+1}. {file_name[:-5]}")
                                    i += 1
                                slice_opt = input("Seleccionar slice: ")
                                file_name = files[int(slice_opt)-1]
                                f = open(f"./Modules/Slices/{file_name}", "r")
                                slice = json.loads(f.read())
                                prox_node = slice["ultimo_nodo"]+1
                                f.close()
                            while True:
                                opt =  o.def_config_slice()
                                if opt == "exit":
                                    break
                                elif int(opt) == 1:
                                    slice["nodos"][f"n{prox_node}"] = {"enlaces":[]}
                                    print(f"* Nodo n{prox_node} agregado.")
                                    prox_node += 1
                                    pass
                                elif int(opt) == 2:
                                    new_slice, new_prox_node = o.draw_subgrafo(slice, prox_node)
                                    slice = new_slice
                                    prox_node = new_prox_node
                                elif int(opt) == 3:
                                    while True:
                                        nodos_dict = slice["nodos"]
                                        i = 1
                                        for node_name in nodos_dict.keys():
                                            print(f"- {node_name}")
                                            i += 1
                                        link = input("Indicar nodos en formato 'n1-n2', escriba 'exit' para terminar: ")
                                        if link == "exit":
                                            break
                                        else:
                                            nodos = link.split("-")
                                            slice["nodos"][nodos[0]]["enlaces"].append(nodos[1])
                                            slice["nodos"][nodos[1]]["enlaces"].append(nodos[0])
                                            print(f"* Enlace {link} creado.")
                                elif int(opt) == 4:
                                    nodos_dict = slice["nodos"]
                                    i = 1
                                    for node_name in nodos_dict.keys():
                                        print(f"- {node_name}")
                                        i += 1
                                    node_opt = input("Indicar nodo que desea borrar: ")
                                    for node_name in slice["nodos"].keys():
                                        enlaces = slice["nodos"][node_name]["enlaces"]
                                        if node_opt in enlaces:
                                            slice["nodos"][node_name]["enlaces"].remove(node_opt)
                                    del slice["nodos"][node_opt]
                                    print(f"* Nodo {node_opt} borrado del slice {slice['nombre']}.")
                                    
                                elif int(opt) == 5:
                                    nodos_dict = slice["nodos"]
                                    print(f"- {nodos_dict}")
                                    i = 1
                                    enlaces_repe=[]
                                    for nodo_origin in nodos_dict:
                                        enlaces_dict=nodos_dict.get(nodo_origin)
                                        for enlaces_array in enlaces_dict.values():
                                            for nodo_enlace in enlaces_array:
                                                if len(enlaces_repe) >0:
                                                    enlace_par=nodo_origin+"-"+nodo_enlace
                                                    if (enlace_par in enlaces_repe):
                                                        print("")
                                                    else:
                                                       print(f"*{nodo_origin}-{nodo_enlace}")
                                                else:
                                                    print(f"*{nodo_origin}-{nodo_enlace}")
                                                enlace = nodo_origin+"-"+nodo_enlace
                                                enlace_inv = nodo_enlace + "-" + nodo_origin
                                                enlaces_repe.append(enlace)
                                                enlaces_repe.append(enlace_inv)
                                        i += 1
                                    enlace_opt = input("Indicar enlace que desea borrar en formato 'n1-n2', escriba 'exit' para terminar: ")
                                    if enlace_opt == "exit":
                                        break
                                    else:
                                        nodos = enlace_opt.split("-")
                                        slice["nodos"][nodos[0]]["enlaces"].remove(nodos[1])
                                        slice["nodos"][nodos[1]]["enlaces"].remove(nodos[0])
                                        print(f"* Enlace {enlace_opt}borrado.")
                                elif int(opt) == 6:
                                    conf_nodos_mode = o.def_conf_nodos1()
                                    if conf_nodos_mode == 'exit':
                                        pass
                                    elif int(conf_nodos_mode) == 1:
                                        nodos_dict = slice["nodos"]
                                        nodos_lista = []
                                        for node_name in nodos_dict.keys():
                                            nodos_lista.append(node_name)
                                        nodos=nodos_lista
                                        print(f"Configurará: {nodos_lista}")
                                        conf_nodos_mode2 = o.def_conf_nodos2()
                                        if conf_nodos_mode == 'exit':
                                            pass
                                        elif int(conf_nodos_mode2) == 1:
                                            # TODO: conexión a base dedatos que devuelve listado de flavors
                                            print("Lista de flavors:")
                                            print("* m1.tiny")
                                            flavor = input("Ingrese el flavor que desea configurar:")
                                            info_config = [flavor]
                                            for nodo in nodos:
                                                type = {"type": "flavor", "info_config": info_config}
                                                slice["nodos"][nodo]["config"] = type
                                            # TODO: conexión a base dedatos que devuelve listado de imagenes
                                            print("***************************************")
                                            print("Lista de imágenes:")
                                            print("* cirros")
                                            imagen = input("Seleccione la imagen que desea configurar:")
                                            info_config = [imagen]
                                            for nodo in nodos:
                                                type = {"imagen": info_config}
                                                slice["nodos"][nodo]["config"]["imagen"] = info_config
                                            print(f"Se configuró los siguientes nodos {nodos} con flavor: {flavor} e imagen: {imagen}")

                                        elif int(conf_nodos_mode2) == 2:
                                            cpu = input("Indicar el # de CPUs:")
                                            ram = input("Indicar la capacidad de la memoria RAM en MB:")
                                            disco = input("Indicar la capacidad de disco en GB:")
                                            info_config = [cpu, ram, disco]
                                            config = {}
                                            for nodo in nodos:
                                                type = {"type": "manual", "info_config": info_config}
                                                slice["nodos"][nodo]["config"] = type
                                            # TODO: conexión a base dedatos que devuelve listado de imagenes
                                            print("***************************************")
                                            print("Lista de imágenes:")
                                            print("* cirros")
                                            imagen = input("Seleccione la imagen que desea configurar:")
                                            info_config = [imagen]
                                            for nodo in nodos:
                                                slice["nodos"][nodo]["config"]["imagen"] = info_config
                                            print(f"Se configuró los siguientes nodos {nodos} con:")
                                            print(f"RAM: {ram} , CPU: {cpu}, DISCO: {disco} e imagen: {imagen}")
                                        else:
                                            print("Opción no válida")
                                    elif int(conf_nodos_mode) == 2:
                                        nodos_dict = slice["nodos"]
                                        i = 1
                                        for node_name in nodos_dict.keys():
                                            print(f"- {node_name}")
                                            i += 1
                                        enlace_opt = input("Indicar nodos que desea borrar en formato 'n1,n2,n3,etc', escriba 'exit' para terminar: ")
                                        if enlace_opt == "exit":
                                            break
                                        else:
                                            nodos = enlace_opt.split(",")
                                            print(f"Configurará: {nodos}")
                                            conf_nodos_mode2 = o.def_conf_nodos2()
                                            if conf_nodos_mode == 'exit':
                                                pass
                                            elif int(conf_nodos_mode2) == 1:
                                                # TODO: conexión a base dedatos que devuelve listado de flavors
                                                print("Lista de flavors:")
                                                print("* m1.tiny")
                                                flavor = input("Ingrese el flavor que desea configurar:")
                                                info_config = [flavor]
                                                for nodo in nodos:
                                                    type = {"type": "flavor", "info_config": info_config}
                                                    slice["nodos"][nodo]["config"] = type
                                                # TODO: conexión a base dedatos que devuelve listado de imagenes
                                                print("***************************************")
                                                print("Lista de imágenes:")
                                                print("* cirros")
                                                imagen = input("Seleccione la imagen que desea configurar:")
                                                info_config = [imagen]
                                                for nodo in nodos:
                                                    type = {"imagen": info_config}
                                                    slice["nodos"][nodo]["config"]["imagen"] = info_config
                                                print(f"Se configuró los siguientes nodos {nodos} con flavor: {flavor} e imagen: {imagen}")
                                            elif int(conf_nodos_mode2) == 2:
                                                cpu = input("Indicar el # de CPUs:")
                                                ram = input("Indicar la capacidad de la memoria RAM en GB:")
                                                disco = input("Indicar la capacidad de disco en GB:")
                                                info_config = [cpu, ram, disco]
                                                config = {}
                                                for nodo in nodos:
                                                    type = {"type": "manual", "info_config": info_config}
                                                    slice["nodos"][nodo]["config"] = type
                                                # TODO: conexión a base dedatos que devuelve listado de imagenes
                                                print("***************************************")
                                                print("Lista de imágenes:")
                                                print("* cirros")
                                                imagen = input("Seleccione la imagen que desea configurar:")
                                                info_config = [imagen]
                                                for nodo in nodos:
                                                    #type = {"imagen": info_config}
                                                    slice["nodos"][nodo]["config"]["imagen"] = imagen
                                                print(f"Se configuró los siguientes nodos {nodos} con:")
                                                print(f"RAM: {ram} , CPU: {cpu}, DISCO: {disco} e imagen: {imagen}")
                                            else:
                                                print("Opción no válida")
                                elif int(opt) == 7:
                                    slice["ultimo_nodo"] = prox_node-1
                                    print("------Data a enviar-----")
                                    print(slice)
                                    o.save_changes(slice, from_scratch)
                                    pass
                                elif int(opt) == 8:
                                    topo = Topology()
                                    print(slice)
                                    topo.draw_topology(slice)
                        else:
                            print("* Opcion no valida.")
                            break
                elif option == 3:
                    while True:
                        nombre_zona_escogida = o.def_borrar_menu1()
                        if nombre_zona_escogida == "exit":
                            break
                        else:
                            while True:
                                slice_escogido = o.def_borrar_menu2()
                                if slice_escogido == "exit":
                                    break
                                else:
                                    confirma_borrado = o.def_borrar_menu3(slice_escogido)
                                    if int(confirma_borrado) == 2:
                                        print("***********************************")
                                        print("No se borró nada")
                                        print("***********************************")
                                    elif int(confirma_borrado) == 1:
                                        print("***********************************")
                                        print("Data enviada a BD \nID de slice = ", 14)
                                        print("Se borró el slice ", slice_escogido)
                                        print("***********************************")
                elif option == 2:
                    while True:
                        nombre_zona_escogida = o.def_listar_menu1()
                        if nombre_zona_escogida == "exit":
                            break
                        else:
                            while True:
                                slice_escogido = o.def_listar_menu2()
                                if slice_escogido == "exit":
                                    break
                                else:
                                    print("***********************************")
                                    print("Detalle del slice", slice_escogido, "en la zona ", nombre_zona_escogida)
                                    print("RAM: 8GB   CPU: 4  #DISCO: 10GB ")
                                    print("***********************************")
                elif option == 4:
                    nombre_zona = o.def_zona_disponibilidad_menu()
                    tipo_zona = o.def_zona_disponibilidad_menu2()
                    tipo_zona = int(tipo_zona)
                    if tipo_zona == 1:
                        server_linux_cluster = []
                        while True:
                            server_escogido,lista = o.def_zona_disponibilidad_menu3()
                            #print("Data enviada a BD \nID de servidor = ", int(server_escogido)+1)
                            if server_escogido == "exit":
                                print("Se registró su zona de disponibilidad" , nombre_zona, " de tipo Linux cluster en los servidores", server_linux_cluster)
                                break
                            else:
                                for dic in lista:
                                    nombre_escogido=dic.pop(server_escogido)
                                    print(f"Server escogido {nombre_escogido}")
                                server_linux_cluster.append(nombre_escogido)
                    elif tipo_zona == 2:
                        server_openstack = []
                        while True:
                            server_escogido,lista = o.def_zona_disponibilidad_menu3()
                            #print("Data enviada a BD \nID de servidor = ", int(server_escogido)+10)
                            if server_escogido == "exit":
                                print("**************************************")
                                print("Se registró su zona de disponibilidad", nombre_zona, " de tipo Openstack en los servidores",
                                      server_openstack)
                                print("**************************************")
                                break
                            else:
                                for dic in lista:
                                    nombre_escogido=dic.pop(server_escogido)
                                    print(f"Server escogido {nombre_escogido}")
                                server_openstack.append(nombre_escogido)
                    else:
                        break
                elif option == 5:
                    o.exit()
                    break
                else:
                    print("Opción no válida")

            except Exception as e:
                print(e)

    @staticmethod
    def create_topology(grafo):
        sliceAdministrator = SliceAdministrator()
        result = sliceAdministrator.create_topology(grafo)