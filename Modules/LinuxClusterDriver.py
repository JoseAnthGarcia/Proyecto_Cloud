
import random
import secrets as s
import requests
from conf.Conexion import *

def generador_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generar_vm_nombre(nodos):
    vm_nombres = {}
    for nodo_key in nodos:
        vm_nombres[nodo_key] = s.token_hex(3)
    return vm_nombres

def linux_driver_main(slice):
    conn = Conexion()
    # VLAN ID actually ranges from 1 to 4094
    vlan_id = 1
    maxvlan = conn.GetMaxVlan()
    #TODO: COMPLETAR
    
    nombre_slice = slice["nombre"]
    conn.Insert("slice", "nombre,tipo,vlan_id,fecha_creacion,fecha_modificacion", f"{nombre_slice},linux_cluster, {}")
    vm_nombres = generar_vm_nombre(slice["nodos"])
    vnc_port = 1
    for nodo_key in slice["nodos"]:
        nodo = slice["nodos"][nodo_key]
        vm_nombre = vm_nombres[nodo_key]
        if nodo["config"]["type"] == "manual":
            recursos = nodo["config"]["info_config"]
            vm_recursos = {"vcpu": int(recursos[0]), "ram": int(recursos[1]), "disk":int(recursos[2])}
        else:
            #   TODO: ver en base de datos el flavor
            vm_recursos = {}
        enlaces=[]
        for i in range(len(nodo["enlaces"])):
            enlaces.append(vm_nombres[nodo["enlaces"][i]])
        imagen = nodo["config"]["imagen"]
        vm_worker_id = nodo["id_worker"]
        enlaces = ",".join(enlaces)
        data = {"vm_nombre": vm_nombre,
                "vm_recursos": vm_recursos,
                "enlaces":enlaces,
                "imagen": imagen,
                "vlan_id": vlan_id,
                "vnc_port": vnc_port,
                "vm_worker_id" : vm_worker_id}
        result = requests.post("http://10.20.12.58:8081/vm/crear", json= data)
        print(result.json())
        vnc_port += 1