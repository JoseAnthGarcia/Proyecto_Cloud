import requests
from conf.Conexion import *
slice={"nodos": {"n0": {"enlaces": ["n1"], "config": {"type": "manual", "info_config": ["1", "256", "1"], "imagen": "cirros"}, "id_worker": 3}, "n1": {"enlaces": ["n0", "n2"], "config": {"type": "manual", "info_config": ["1", "256", "1"], "imagen": "cirros"}, "id_worker": 3}, "n2": {"enlaces": ["n1"], "config": {"type": "manual", "info_config": ["1", "256", "1"], "imagen": "cirros"}, "id_worker": 3}}, "nombre": "prueba1", "ultimo_nodo": 1, "zona": {"nombre": "Pabellon V"}, "nodo_eliminar":"n0", "mapeo_nombre":{"n0":"ccc","n1":"ddd","n2":"eee"}}

#del(data["nodos"]["n0"])
#print(data)
#print(data["nodos"]["n0"]["enlaces"])


#for nodo in data["nodos"].values():
#    print(nodo)
    #if("n0" in nodo["enlaces"]):
    #    data["nodos"][nodo]["enlace"]

################### GENERACIÓN DEL NUEVO JSON #############################
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
result = requests.post("http://10.20.12.58:8081/vm/borrar?worker_id="+vm_worker_id+"&vm_name="+nombre_vm+"&taps="+taps)
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




