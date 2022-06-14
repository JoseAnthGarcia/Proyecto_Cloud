class Topology:
    def __init__(self):
        pass

    def create_start_topology(self, nodos):
        i = 0
        array_nodos = []
        for i in range(nodos + 1):
            i = i + 1
            nodo = "n" + str(i)
            array_nodos.append(nodo)
        print(array_nodos)
        j = 0
        json_topology = []
        for k in range(nodos + 1):
            if k == 1:
                nodos_enlaces = []
                for i in range(nodos):
                    nodos_enlaces.append(array_nodos[i + 1])
                    i = i + 1
                    nodo = {"enlaces": nodos_enlaces}
                    json_nodo = {array_nodos[k - 1]: {"enlaces": nodos_enlaces}}
                json_topology.append(json_nodo)
            else:
                nodos_enlaces = []
                nodos_enlaces.append(array_nodos[0])
                nodo = {"enlaces": nodos_enlaces}
                json_nodo = {array_nodos[k - 1]: {"enlaces": nodos_enlaces}}
                json_topology.append(json_nodo)
            k = k + 1
        return json_topology

    def create_lineal_topology(self, nodos):
        i = 0
        array_nodos = []
        for i in range(nodos):
            i = i + 1
            nodo = "n" + str(i)
            array_nodos.append(nodo)
        print(array_nodos)
        j = 0
        json_topology = []
        for k in range(nodos):
            print(k)
            if k == 0:
                nodos_enlaces = []
                nodos_enlaces.append(array_nodos[k + 1])
                json_nodo = {array_nodos[k]: {"enlaces": nodos_enlaces}}
                json_topology.append(json_nodo)
            elif k == nodos-1:
                nodos_enlaces = []
                nodos_enlaces.append(array_nodos[k - 1])
                json_nodo = {array_nodos[k]: {"enlaces": nodos_enlaces}}
                json_topology.append(json_nodo)
            else:
                print(k)
                nodos_enlaces = []
                nodos_enlaces.append(array_nodos[k-1])
                nodos_enlaces.append(array_nodos[k + 1])
                json_nodo = {array_nodos[k]: {"enlaces": nodos_enlaces}}
                json_topology.append(json_nodo)
            k = k + 1
        return json_topology
        pass

    def create_ring_topology(self, nodos):
        i = 0
        array_nodos = []
        for i in range(nodos):
            i = i + 1
            nodo = "n" + str(i)
            array_nodos.append(nodo)
        print(array_nodos)
        j = 0
        json_topology = []
        for k in range(nodos):
            if k == 0:
                nodos_enlaces = []
                nodos_enlaces.append(array_nodos[k + 1])
                nodos_enlaces.append(array_nodos[nodos-1])
                json_nodo = {array_nodos[k]: {"enlaces": nodos_enlaces}}
                json_topology.append(json_nodo)
            elif k == nodos-1:
                nodos_enlaces = []
                nodos_enlaces.append(array_nodos[k - 1])
                nodos_enlaces.append(array_nodos[0])
                json_nodo = {array_nodos[k]: {"enlaces": nodos_enlaces}}
                json_topology.append(json_nodo)
            else:
                nodos_enlaces = []
                nodos_enlaces.append(array_nodos[k-1])
                nodos_enlaces.append(array_nodos[k + 1])
                json_nodo = {array_nodos[k]: {"enlaces": nodos_enlaces}}
                json_topology.append(json_nodo)
            k = k + 1
        return json_topology
        pass

    def create_malla_topology(self,filas,columnas):
        nodos = filas * columnas
        i = 0
        array_nodos = []
        array_total=[]
        for i in range(filas):
            i = i + 1
            array_parcial = []
            for j in range(columnas):
                j=j+1
                nodo = "n" + str(i)
                nodo = nodo + str(j)
                array_nodos.append(nodo)
                array_parcial.append(nodo)
            array_total.append(array_parcial)
        print(array_nodos)
        print(array_total)
        k = 0
        json_topology = []
        for k in range(filas):
            for j in range(columnas):
                if k == 0:
                    #primera fila
                    if j == 0:
                        nodos_enlaces = []
                        nodos_enlaces.append(array_total[k + 1][j])
                        nodos_enlaces.append(array_total[k][j+1])
                        json_nodo = {array_total[k][j]: {"enlaces": nodos_enlaces}}
                        json_topology.append(json_nodo)
                    elif j == columnas-1:
                        nodos_enlaces = []
                        nodos_enlaces.append(array_total[k + 1][j])
                        nodos_enlaces.append(array_total[k][j - 1])
                        json_nodo = {array_total[k][j]: {"enlaces": nodos_enlaces}}
                        json_topology.append(json_nodo)
                    else:
                        nodos_enlaces = []
                        nodos_enlaces.append(array_total[k + 1][j])
                        nodos_enlaces.append(array_total[k][j - 1])
                        nodos_enlaces.append(array_total[k][j + 1])
                        json_nodo = {array_total[k][j]: {"enlaces": nodos_enlaces}}
                        json_topology.append(json_nodo)
                elif k==filas-1:
                    # ultima fila
                    if j == 0:
                        nodos_enlaces = []
                        nodos_enlaces.append(array_total[k - 1][j])
                        nodos_enlaces.append(array_total[k][j + 1])
                        json_nodo = {array_total[k][j]: {"enlaces": nodos_enlaces}}
                        json_topology.append(json_nodo)
                    elif j == columnas - 1:
                        nodos_enlaces = []
                        nodos_enlaces.append(array_total[k - 1][j])
                        nodos_enlaces.append(array_total[k][j - 1])
                        json_nodo = {array_total[k][j]: {"enlaces": nodos_enlaces}}
                        json_topology.append(json_nodo)
                    else:
                        nodos_enlaces = []
                        nodos_enlaces.append(array_total[k - 1][j])
                        nodos_enlaces.append(array_total[k][j - 1])
                        nodos_enlaces.append(array_total[k][j + 1])
                        json_nodo = {array_total[k][j]: {"enlaces": nodos_enlaces}}
                        json_topology.append(json_nodo)
                else:
                    # filas intermedias
                    if j == 0:
                        nodos_enlaces = []
                        nodos_enlaces.append(array_total[k + 1][j])
                        nodos_enlaces.append(array_total[k - 1][j])
                        nodos_enlaces.append(array_total[k][j + 1])
                        json_nodo = {array_total[k][j]: {"enlaces": nodos_enlaces}}
                        json_topology.append(json_nodo)
                    elif j == columnas - 1:
                        print(k)
                        nodos_enlaces = []
                        nodos_enlaces.append(array_total[k + 1][j])
                        nodos_enlaces.append(array_total[k - 1][j])
                        nodos_enlaces.append(array_total[k][j - 1])
                        json_nodo = {array_total[k][j]: {"enlaces": nodos_enlaces}}
                        json_topology.append(json_nodo)
                    else:
                        nodos_enlaces = []
                        nodos_enlaces.append(array_total[k + 1][j])
                        nodos_enlaces.append(array_total[k - 1][j])
                        nodos_enlaces.append(array_total[k][j - 1])
                        nodos_enlaces.append(array_total[k][j + 1])
                        json_nodo = {array_total[k][j]: {"enlaces": nodos_enlaces}}
                        json_topology.append(json_nodo)
        return json_topology
        pass

    def create_tree_topology(self,lastNumber, degree):
        start = lastNumber + 1
        N = degree
        sub_grafo = {}
        node = 0
        for k in range(1, N+1):
            nodes_cant = 2**(k-1)
            for i in range(nodes_cant):
                node_name = f"n{node+start}"
                if k == N:
                    enlaces = []
                else:
                    enlaces = [f"n{node*2+1+start}", f"n{node*2+2+start}"]
                sub_grafo[node_name] = {"enlaces": enlaces}
                # nodes.append({node_name:{"enlaces": enlaces}})
                # print(f"Node: {node_name}")
                # print(f"Enlaces: {enlaces}")
                node += 1
        return sub_grafo

topo = Topology()