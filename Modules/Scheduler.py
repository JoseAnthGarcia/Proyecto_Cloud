import pymysql

lista_worker_general_filtrada=[]

class Worker:
    def __init__ (self, id_servidor,ram_disponible, disco_disponible, vcpu_disponible, ram, disco, vcpu):
        self.id_servidor=id_servidor
        self.ram_disponible=ram_disponible
        self.disco_disponible=disco_disponible
        self.vcpu_disponible=vcpu_disponible
        self.ram=ram
        self.disco=disco
        self.vcpu=vcpu

class Vm:
    def __init__ (self, ram_requerida, disco_requerido, vcpu_requeridas):
        self.ram_requerida=ram_requerida
        self.disco_requerido=disco_requerido
        self.vcpu_requeridas=vcpu_requeridas



def filtrado(zona_disponibilidad):
    #Hacer select de todos los workers y filtrarlos (query con un where zona_disponibilidad =)#
    query="select s.id_servidor, r.ram_available, r.storage_available, r.vcpu_available, r.ram, r.storage, r.vcpu from recursos as r inner join servidor as s on s.id_recurso=r.id_recursos inner join zona_disponibilidad as zd on zd.idzona_disponibilidad=s.id_zona where zd.nombre="+zona_disponibilidad

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
            worker=Worker(f[0],f[1],f[2],f[3],f[4],f[5],f[6])
            lista_worker_general_filtrada.append(worker)
    finally:
	    con.close()


def takeSecond(elem):
    print(elem)
    return elem[0]


def calculo_coeficiente(ram_disponible, disco_disponible, vcpu_requeridas, vcpu_disponible,ram,disco):
    coeficiente = 0.5*(ram_disponible/ram)+0.25*(disco_disponible/disco) + 0.25*(vcpu_requeridas/vcpu_disponible)
    return coeficiente

def ordenamiento_coeficiente(lista_worker_general_filtrada,vm):

    #lista_worker=[]
    lista_worker_coeficiente=[]
    lista_worker_ordenada=[]
    lista_worker_ordenadas_par=[]
    
    contador=0
    #lista_worker_filtradas=filtrado()
    w = 0
    for worker in lista_worker_general_filtrada:
        coeficiente= calculo_coeficiente(worker.ram_disponible, worker.disco_disponible, vm.vcpu_requeridas, worker.vcpu_disponible,worker.ram,worker.disco)
        #par=[coeficiente,worker]
        par=[coeficiente,w]
        lista_worker_coeficiente.append(par)
        w += 1
    
    print(lista_worker_coeficiente)
  
    lista_worker_coeficiente.sort(key=takeSecond, reverse = True)
    
    print((lista_worker_coeficiente))
    for par in lista_worker_coeficiente:
        lista_worker_ordenada.append(lista_worker_general_filtrada[par[1]])
    for worker in lista_worker_ordenada:
        if (worker.ram_disponible >= vm.ram_requerida and worker.disco_disponible >= vm.disco_requerido and worker.vcpu_disponible >= vm.vcpu_requeridas):
            worker_elegido = worker
            worker_nuevo = worker_elegido
            ram_disponible_new= worker.ram_disponible - vm.ram_requerida
            disco_disponible_new = worker.disco_disponible - vm.disco_requerido
            vcpu_total_new= worker.vcpu_disponible - vm.vcpu_requeridas
            worker_nuevo.ram_disponible=ram_disponible_new
            worker_nuevo.disco_disponible=disco_disponible_new
            worker_nuevo.vcpu_disponible=vcpu_total_new
            lista_worker_general_filtrada= lista_worker_ordenada
            lista_worker_general_filtrada[contador]=worker_nuevo
            break
        else :
            print ('## No es posible instancia esta topología ##')
            worker_elegido = 0
        
        contador= contador+1
    return worker_elegido



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
    "zona": {"nombre": "Pabellón V"}}

    #VCPU-RAM-STORAGE
lista_vm_topologia=[]
nodos=data['nodos']
for n in nodos.values():
    if (n['config']['type'] == 'manual'):
        vcpu=n['config']['info_config'][0]
        ram=n['config']['info_config'][1]
        storage=n['config']['info_config'][2]
        vm=Vm(int(ram),int(storage),int(vcpu))
        lista_vm_topologia.append(vm)

zona_disponibilidad= data['zona']['nombre']
lista_worker_general_filtrada=filtrado(zona_disponibilidad)
    
for vm in lista_vm_topologia:
    worker_elegido= ordenamiento_coeficiente(lista_worker_general_filtrada,vm)
    print(worker_elegido.id_servidor)