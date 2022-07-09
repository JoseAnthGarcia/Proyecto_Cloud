import pymysql
import requests

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
    def __init__ (self,nodo_nombre , ram_requerida, disco_requerido, vcpu_requeridas):
        self.nodo_nombre = nodo_nombre
        self.ram_requerida=ram_requerida
        self.disco_requerido=disco_requerido
        self.vcpu_requeridas=vcpu_requeridas



def filtrado(zona_disponibilidad, FACTOR):

    #Hacer select de todos los workers y filtrarlos (query con un where zona_disponibilidad =)#
    query="select s.id_servidor, r.ram_available, r.storage_available, r.vcpu_available, r.ram, r.storage, r.vcpu from recursos as r inner join servidor as s on s.id_recurso=r.id_recursos inner join zona_disponibilidad as zd on zd.idzona_disponibilidad=s.id_zona where zd.nombre= "+zona_disponibilidad

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
            worker=Worker(f[0],f[1]*FACTOR,f[2]*FACTOR,f[3]*FACTOR,f[4]*FACTOR,f[5]*FACTOR,f[6]*FACTOR)
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


def scheduler_main(data, FACTOR):
    #Actualizamos los valores en base de datos: mas adelante esto lo hara el validador
    x = requests.get('http://10.20.12.58:8081/cpu-metrics')
    #VCPU-RAM-STORAGE
    lista_vm_topologia=[]
    nodos=data['nodos']
    for nodo_key in nodos:
        if (nodos[nodo_key]['config']['type'] == 'manual'):
            vcpu=nodos[nodo_key]['config']['info_config'][0]
            ram=nodos[nodo_key]['config']['info_config'][1]
            storage=nodos[nodo_key]['config']['info_config'][2]
            vm=Vm(nodo_key ,int(ram),int(storage),int(vcpu))
            lista_vm_topologia.append(vm)

    zona_disponibilidad= data['zona']['nombre']
    lista_worker_general_filtrada=filtrado(zona_disponibilidad, FACTOR)
        
    for vm in lista_vm_topologia:
        worker_elegido= ordenamiento_coeficiente(lista_worker_general_filtrada,vm)
        data["nodos"][vm.nodo_nombre] = worker_elegido.id_servidor
        print(data)
        print("---------------------------------------------------")

    return data