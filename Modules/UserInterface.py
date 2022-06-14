from Topology import *
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
        print('Lista de servidores disponibles:')
        print('1. Server 1')
        print('2. Server 2')
        print('3. Server 3')
        print('4. Server 4')
        print("Escriba 'exit' si terminó de escoger los servidores para su zona de disponibilidad")
        return input('Opción: ')

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
    def draw_subgrafo(last_node_number):
        topology = Topology()
        print("Escoja la topología del subgrafo que desea agregar:")
        print("a. lineal")
        print("b. malla")
        print("c. árbol")
        print("d. anillo")
        print("e. bus")
        print("f. estrella")
        topo_type = input('Opción: ')
        if topo_type == "a":
            # TODO: printear ingreso de valor segun sea el tipo
            pass
        elif topo_type == "c":
            nivel = int(input("Ingrese el numeros de niveles:"))
            subtopology = topology.create_tree_topology(last_node_number, nivel)
            print(subtopology)



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
                            number = 0
                            if int(config_mode) == 1:
                                slice_name = input("Nombre del slice: ")
                                slice["nombre"] = slice_name
                                print(f"* Slice {slice_name} creado.")
                            else:
                                #TODO: Listar los slices creados anteriormente
                                pass
                            while True:
                                opt =  o.def_config_slice()
                                if opt == "exit":
                                    break
                                elif int(opt) == 1:
                                    slice["nodos"][f"n{number}"] = {"enlaces":[]}
                                    print(f"* Nodo n{number} agregado.")
                                    number += 1
                                    pass
                                elif int(opt) == 2:
                                    o.draw_subgrafo(number)
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
                                    pass
                                elif int(opt) == 6:
                                    pass
                                elif int(opt) == 7:
                                    pass
                                elif int(opt) == 8:
                                    print(slice)
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
                                    print("RAM:   CPU:   #DISCO:  ")
                                    print("***********************************")
                elif option == 4:
                    nombre_zona = o.def_zona_disponibilidad_menu()
                    tipo_zona = o.def_zona_disponibilidad_menu2()
                    tipo_zona = int(tipo_zona)
                    if tipo_zona == 1:
                        server_linux_cluster = []
                        while True:
                            server_escogido = o.def_zona_disponibilidad_menu3()
                            if server_escogido == "exit":
                                print("Se registró su zona de disponibilidad" , nombre_zona, " de tipo Linux cluster en los servidores", server_linux_cluster)
                                break
                            else:
                                server_linux_cluster.append(server_escogido)
                    elif tipo_zona == 2:
                        server_openstack = []
                        while True:
                            server_escogido = o.def_zona_disponibilidad_menu3()
                            if server_escogido == "exit":
                                print("**************************************")
                                print("Se registró su zona de disponibilidad", nombre_zona, " de tipo Openstack en los servidores",
                                      server_openstack)
                                print("**************************************")
                                break
                            else:
                                server_openstack.append(server_escogido)
                    else:
                        break
                elif option == 5:
                    o.exit()
                    break
                else:
                    print("Opción no válida")

            except Exception as e:
                print(e)

# UserInterface.iniciar_programa()