
class Orquestador:
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
        print('1.Configuración desde cero')
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
    def validate_option(option):
        if not((option > 0) and (option < 100)):
            raise Exception('Invalid option')
        else:
            return True

    @staticmethod
    def exit(self):
        self.service.con.close()
        print('Elaborado por GRUPO 1\n')

    @staticmethod
    def iniciar_programa():
        o = Orquestador()
        while True:
            print('*********************************')
            print('')
            option = Orquestador.main_menu()
            try:
                option = int(option)
                Orquestador.validate_option(option)

                if option == 1:
                    while True:
                        config_mode = o.def_conf_menu1()
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

Orquestador.iniciar_programa()