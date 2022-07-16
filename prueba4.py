import requests
from conf.Conexion import *
data={"nodos": {"n0": {"enlaces": ["n1"], "config": {"type": "manual", "info_config": ["1", "256", "1"], "imagen": "cirros"}, "id_worker": 3}, "n1": {"enlaces": ["n0", "n2"], "config": {"type": "manual", "info_config": ["1", "256", "1"], "imagen": "cirros"}, "id_worker": 3}, "n2": {"enlaces": ["n1"], "config": {"type": "manual", "info_config": ["1", "256", "1"], "imagen": "cirros"}, "id_worker": 3}}, "nombre": "prueba1", "ultimo_nodo": 1, "zona": {"nombre": "Pabellon V"}, "nodo_eliminar":"n0"}

#del(data["nodos"]["n0"])
#print(data)
#print(data["nodos"]["n0"]["enlaces"])


#for nodo in data["nodos"].values():
#    print(nodo)
    #if("n0" in nodo["enlaces"]):
    #    data["nodos"][nodo]["enlace"]

################### GENERACIÓN DEL NUEVO JSON #############################
print(data)
for nodo in list(data["nodos"]):
    if (data["nodo_eliminar"] in data["nodos"][nodo]["enlaces"]):
        data["nodos"][nodo]["enlaces"].remove(data["nodo_eliminar"])
    if data["nodo_eliminar"]==nodo:
        del data["nodos"][nodo]
        vm_worker_id = nodo["id_worker"]
print("---------------------------------------------------------------------")
print(data)

################### BORRADO EN EL HEADNODE #############################
enviar = {"worker_id": vm_worker_id,
                "vm_name": "vm-8b6d9b", #¿como obtengo eso?
                "taps":"866d47", #¿cómo obtengo ese nombre de taps?, ¿donde se guarda?
                }
result = requests.post("http://10.20.12.58:8081/vm/borrar", json= data)
print(result.json())

################### BORRADO EN LA BD #############################

if (result):
    conn= Conexion()
    conn2=Conexion2()
    id_nodo_general= conn.Select("id_vm","vm","nombre= "+enviar["name"])
    id_recurso_general= conn.Select("recursos_id_estado","vm","nombre= "+enviar["name"])
    conn.Delete("recursos","id_recursos= "+id_recurso_general)
    conn.Delete("vm","id_vm= "+id_nodo_general)
    id_nodo_cluster=conn2.Select("id_nodo","nodo","nombre= "+enviar["name"])
    conn2.Delete("nodo", "nombre= "+enviar["vm_name"])
    conn2.Delete("enlace","nodo_id_nodo= "+id_nodo_cluster)




