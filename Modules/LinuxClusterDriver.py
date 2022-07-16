
import random
import secrets as s
import requests
from conf.Conexion import *
from datetime import datetime

def generador_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generar_vm_token(nodos):
    vm_nombres = {}
    for nodo_key in nodos:
        vm_nombres[nodo_key] = s.token_hex(3)
    return vm_nombres

def linux_driver_main(slice):
    fecha_actual= datetime.today()
    conn = Conexion()
    conn2= Conexion2()
    # VLAN ID actually ranges from 1 to 4094
    vlan_id = 1
    maxvlan= conn.GetMaxVlan()
    maxvlan=maxvlan[0][0]
    if maxvlan==None:
        maxvlan=0
    print(type(maxvlan))
    print(maxvlan)
    #TODO: COMPLETAR
    vlan=maxvlan+1
    nombre_slice = slice["nombre"]
    id_slice=conn.Insert("slice", "nombre,tipo,vlan_id,fecha_creacion,fecha_modificacion", f"'{nombre_slice}','linux_cluster',{vlan},now(),now()")
    vm_nombres = generar_vm_token(slice["nodos"])
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
        data = {"vm_token": vm_nombre,
                "vm_recursos": vm_recursos,
                "enlaces":enlaces,
                "imagen": imagen,
                "vlan_id": vlan_id,
                "vnc_port": vnc_port,
                "vm_worker_id" : vm_worker_id}
        result = requests.post("http://10.20.12.58:8081/vm/crear", json= data)
        print(result.json())
        if (result):
            #AGREGAR PARÁMETROS A BD
            #--------CREACIÓN DE TABLA RECURSOS--------#
            ram= vm_recursos["ram"]
            disk=vm_recursos["disk"]
            vcpu=vm_recursos["vcpu"]
            nombre="vm-"+data["vm_token"]
            
            id_recursos=conn.Insert("recursos", "ram,storage,vcpu", f"'{ram}','{disk}','{vcpu}'")

            id_vm=conn.Insert("vm", "nombre,estado,fecha_creacion,creado_por,fecha_modificacion,modificado_por,vnc,servidor_id_servidor,topologia_id_topologia,imagen_id_imagen,recursos_id_estado", f"'{nombre}','ACTIVO',now(),1,now(),1,{vnc_port},{vm_worker_id},{id_slice},1,{id_recursos}")

            id_nodo=conn2.Insert("nodo", "nombre,tipo,puerto_vnc", f"'{nombre}',1,{vnc_port}")
            id_ram=conn2.Insert("ram", "memoria_total, creacion, Nodo_id_nodo", f"'{ram}',now(),{id_nodo}")
            id_cpu=conn2.Insert("cpu", "memoria_total, creacion, Nodo_id_nodo", f"'{disk}',now(),{id_nodo}")
            id_vcpu=conn2.Insert("vcpu", "vcpu_total, creacion, Nodo_id_nodo", f"'{vcpu}',now(),{id_nodo}")
            id_enlace=conn2.Insert("enlace", "nombre,nodo_id_nodo", f"'{enlaces}',{id_nodo}")
            
        else:
            print("Falló la creación de la vm "+ data["vm_nombre"])
        vnc_port += 1
    slice["mapeo_nombres"] = vm_nombres
    return slice
    
def borrar_nodo(slice):
    for nodo in list(slice["nodos"]):
        if (slice["nodo_eliminar"] in slice["nodos"][nodo]["enlaces"]):
            slice["nodos"][nodo]["enlaces"].remove(slice["nodo_eliminar"])
        if slice["nodo_eliminar"]==nodo:
            nombre_vm= slice["mapeo_nombre"][nodo]
            vm_worker_id = slice["nodos"][nodo]["id_worker"]
            nombre_nodo=nodo
            #print(nombre_vm)
            #print(vm_worker_id)
            del slice["nodos"][nodo]
    print("---------------------------------------------------------------------")
    print(slice)
    ################### BORRADO EN EL HEADNODE #############################

    conn2=Conexion2()
    id_nodo_cluster=conn2.Select("id_nodo","nodo","nombre= "+nombre_vm)
    taps=conn2.Select("nombre","enlace","nodo_id_nodo= "+id_nodo_cluster)
    result = requests.get("http://10.20.12.58:8081/vm/borrar?worker_id="+vm_worker_id+"&vm_name="+nombre_vm+"&taps="+taps)
    print(result.json())
    ################### BORRADO EN LA BD #############################

    if (result):
        conn= Conexion()
        id_nodo_general= conn.Select("id_vm","vm","nombre= "+nombre_vm)
        id_recurso_general= conn.Select("recursos_id_estado","vm","nombre= "+nombre_vm)
        conn.Delete("recursos","id_recursos= "+id_recurso_general)
        conn.Delete("vm","id_vm= "+id_nodo_general)
        conn2.Delete("nodo", "nombre= "+nombre_vm)
        conn2.Delete("enlace","nodo_id_nodo= "+id_nodo_cluster)


    

    