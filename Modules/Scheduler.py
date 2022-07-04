import pymysql

"""
class Scheduler:
    def __init__(self):
        pass

    def decisor(delf, grafo):
        zona_nombre = grafo["zona"]["nombre"]
        # hots = 
        pass

    def db_connection(self, zona):
        pass
"""
lista_worker_general_filtrada=[]

class Worker:
    def __init__ (self, id_servidor,ram_disponible, disco_disponible, vcpu_total):
        self.id_servidor=id_servidor
        self.ram_disponible=ram_disponible
        self.disco_disponible=disco_disponible
        self.vcpu_total=vcpu_total

class Vm:
    def __init__ (self, ram_requerida, disco_requerido, vcpu_requeridas):
        self.ram_requerida=ram_requerida
        self.disco_requerido=disco_requerido
        self.vcpu_requeridas=vcpu_requeridas



def filtrado(zona_disponibilidad):
    #Hacer select de todos los workers y filtrarlos (query con un where zona_disponibilidad =)#
    query="select s.id_servidor, r.ram_available, r.storage_available, r.vcpu_available from recursos as r inner join servidor as s on s.recursos_id_estado=r.id_estado inner join zona_disponibilidad as zd on zd.idzona_disponibilidad=s.zona_disponibilidad_idzona_disponibilidad where zd.nombre= "+zona_disponibilidad

    ip="10.20.12.35"
    username="grupo1_final"
    paswd="grupo1_final"
    database="bd_general"
    con = pymysql.connect(host=ip,user= username,password=paswd, db=database)
    resultado=[]
    try:
        with con.cursor() as cur1:
            cur1.execute(query)
        resultado1 = cur1.fetchall()

        for f in resultado1:
            worker=Worker(f[0],f[1],f[2],f[3])
            lista_worker_general_filtrada.append(worker)
    finally:
	    con.close()


def calculo_coeficiente(ram_disponible, disco_disponible, vcpu_requeridas, vcpu_total):
    coeficiente = 0.5*(ram_disponible/100)+ 0.25*(disco_disponible/100) + 0.25*(vcpu_requeridas/vcpu_total)
    return coeficiente

def ordenamiento_coeficiente(vm, lista_worker_general_filtrada):

    #lista_worker=[]
    lista_worker_coeficiente=[]
    lista_worker_ordenada=[]
    lista_worker_ordenadas_par=[]
    
    contador=0
    #lista_worker_filtradas=filtrado()
    for worker in lista_worker_general_filtrada:
        coeficiente= calculo_coeficiente(worker.ram_disponible, worker.disco_disponible, vm.vcpu_requeridas, worker.vcpu_total)
        par=[coeficiente,worker]
        lista_worker_coeficiente.append(par)
    lista_worker_ordenadas_par=lista_worker_coeficiente.sort(reverse=True)
    for par in lista_worker_ordenadas_par:
        lista_worker_ordenada.append(par[1])
    for worker in lista_worker_ordenada:
        if (worker.ram_disponible > vm.ram_requerida and worker.disco_disponible > vm.disco_requerido and worker.vcpu_total > vm.cpu_requeridas):
            worker_elegido = worker
            worker_nuevo = worker_elegido
            ram_disponible_new= worker.ram_disponible - vm.ram_requerida
            disco_disponible_new = worker.disco_disponible - vm.disco_requerido
            vcpu_total_new= worker.vcpu_total - vm.cpu_requeridas
            worker_nuevo.ram_disponible=ram_disponible_new
            worker_nuevo.disco_disponible=disco_disponible_new
            worker_nuevo.vcpu_total=vcpu_total_new
            lista_worker_general_filtrada= lista_worker_ordenada
            lista_worker_general_filtrada[contador]=worker_nuevo
            break
        else :
            print ('## No es posible instancia esta topología ##')
            worker_elegido = 0
        
        contador= contador+1
    return worker_elegido

def scheduler():
    #########falta añadir campo de zona al json#########

    data= {"nodos": {"n0": {"enlaces": ["n1"],
                "config": {"type": "manual", "info_config": ["1", "1", "1"], "imagen": "cirros"}},                          
            "n1": {"enlaces": ["n0"],
                    "config": {"type": "flavor", "info_config": ["m1.tyny"], "imagen": ["cirros"]}},
            "n2": {"enlaces": ["n3", "n4"],
                    "config": {"type": "flavor", "info_config": ["m1.tyny"], "imagen": ["cirros"]}},
            "n3": {"enlaces": ["n5", "n6", "n2"],
                    "config": {"type": "manual", "info_config": ["1", "1", "1"], "imagen": "cirros"}},
            "n4": {"enlaces": ["n7", "n8", "n2"],
                    "config": {"type": "flavor", "info_config": ["m1.tyny"], "imagen": ["cirros"]}},
            "n5": {"enlaces": ["n3"],
                    "config": {"type": "flavor", "info_config": ["m1.tyny"], "imagen": ["cirros"]}},
            "n6": {"enlaces": ["n3"],
                    "config": {"type": "flavor", "info_config": ["m1.tyny"], "imagen": ["cirros"]}},
            "n7": {"enlaces": ["n4"],
                    "config": {"type": "manual", "info_config": ["1", "1", "1"], "imagen": "cirros"}},
            "n8": {"enlaces": ["n4"],
                    "config": {"type": "flavor", "info_config": ["m1.tyny"], "imagen": ["cirros"]}}},
    "nombre": "tel142",
    "ultimo_nodo": 8,
    "zona": {"nombre": "zona1"}}

    #VCPU-RAM-STORAGE
    lista_vm_topologia=[]
    nodos=data['nodos']
    for n in nodos.values():
        if (n['config']['type'] == 'manual'):
            vcpu=n['config']['info_config'][0]
            ram=n['config']['info_config'][1]
            storage=n['config']['info_config'][2]
            vm=Vm(ram,storage,vcpu)
            lista_vm_topologia.append(vm)

    zona_disponibilidad= data['zona']['nombre']
    lista_worker_general_filtrada=filtrado(zona_disponibilidad)
    
    for vm in lista_vm_topologia:
        worker_elegido= ordenamiento_coeficiente(lista_worker_general_filtrada,vm)
        print(worker_elegido)






