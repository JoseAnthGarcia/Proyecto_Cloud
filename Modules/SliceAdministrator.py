
from Modules.Scheduler import *
from conf.Conexion import *
from Modules.Validador import  *

class SliceAdministrator:
    def __init__(self):
        pass

    def create_topology(self, grafo):
        FACTOR = 2
        nuevo_grafo = scheduler_main(grafo, FACTOR)
        return nuevo_grafo

    def delete_slice(self,slice):
        conn = Conexion()
        id = conn.Select("id_slice", "slice", f" nombre = {slice}")
        vms= conn.Select("nombre,estado","vm", f" topologia_id_topologia = {id[0]}")
        lista_activo=[]
        lista_inactivo=[]
        message=""
        for vm in vms:
            val = validador.validar_estado_vm(vm[0])
            if val == 'Inactivo':
                lista_inactivo.append(vm[0])
            elif val == 'Activo':
                lista_activo.append(vm[0])

        if len(lista_inactivo) == len(vms):
            for vm in vms:
                conn.Delete("vm", f" topologia_id_topologia = {vm[0]}")
            conn.Delete("slice", f" nombre = {slice}")
            message = f"Se borró el slice {slice} y sus respectivas VMs"
        else:
            message = f"No se pudo borrar el slice {slice} porque las VMs: {lista_activo} están activas."
        return message