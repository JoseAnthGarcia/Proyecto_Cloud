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
    def __init__ (self, ram_disponible, disco_disponible, vcpu_total):
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
    ################################
    #Insertar código para filtrar#
    ################################
    return lista_worker_general_filtrada

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
    data= {"nodos": {"n0": {"enlaces": []}, "n1": {"enlaces": []}, "n3": {"enlaces": ["n4"], "config": {"type": "flavor", "info_config": ["m1.tiny"], "imagen": ["cirros"]}}, "n4": {"enlaces": ["n3", "n5"], "config": {"type": "flavor", "info_config": ["m1.tiny"], "imagen": ["cirros"]}}, "n5": {"enlaces": ["n4"], "config": {"type": "flavor", "info_config": ["m1.tiny"], "imagen": ["cirros"]}}, "Mn77": {"enlaces": ["Mn87", "Mn78"]}, "Mn78": {"enlaces": ["Mn88", "Mn77", "Mn79"]}, "Mn79": {"enlaces": ["Mn89", "Mn78", "n37"]}, "Mn87": {"enlaces": ["Mn97", "Mn77", "Mn88"]}, "Mn88": {"enlaces": ["Mn98", "Mn78", "Mn87", "Mn89"]}, "Mn89": {"enlaces": ["Mn79", "Mn88"]}, "Mn97": {"enlaces": ["Mn87", "Mn98", "n21"]}, "Mn98": {"enlaces": ["Mn88", "Mn97"]}, "n16": {"enlaces": ["n17", "n18"]}, "n17": {"enlaces": ["n19", "n20", "n16"]}, "n18": {"enlaces": ["n21", "n22", "n16"]}, "n19": {"enlaces": ["n17"]}, "n20": {"enlaces": ["n17"]}, "n21": {"enlaces": ["n18", "Mn97"]}, "n22": {"enlaces": ["n18"]}, "n24": {"enlaces": ["n25", "n26"]}, "n25": {"enlaces": ["n24", "n26"]}, "n26": {"enlaces": ["n25", "n24"]}, "n31": {"enlaces": ["n28"]}, "n28": {"enlaces": ["n29", "n30", "n31"]}, "n29": {"enlaces": ["n28"]}, "n30": {"enlaces": ["n28"]}, "n37": {"enlaces": ["n33", "Mn79"]}, "n33": {"enlaces": ["n34", "n35", "n36", "n37"]}, "n34": {"enlaces": ["n33"]}, "n35": {"enlaces": ["n33"]}, "n36": {"enlaces": ["n33"]}}, "nombre": "tel141", "ultimo_nodo": 37}

    zona_disponibilidad= data['zona']
    lista_worker_general_filtrada=filtrado(zona_disponibilidad)
    lista_vm_topologia=[]
    for vm in lista_vm_topologia:
        worker_elegido= ordenamiento_coeficiente(lista_worker_general_filtrada,vm)






