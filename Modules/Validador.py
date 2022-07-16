import requests
import json
import pymysql
import schedule
import time
import datetime
from conf.Conexion import *
from Modules.Scheduler import *

class Validador:
    def __init__(self):
        pass

    def validar_recursos(self, nombre,recursos):
        validador= Validador()
        data_actual = validador.obtenerDataActual()
        data_actual = data_actual[nombre]
        ram_actual = data_actual["ram"]
        vcpu_actual = data_actual["vcpu"]
        storage_actual = data_actual["storage"]
        valid = False
        if vcpu_actual > recursos[0] & ram_actual > recursos[1] &  storage_actual > recursos[2]:
            valid = True
        return valid


    def validar_estado_vm(delf, vm):
        con = Conexion()
        estado_vm = con.Select("estado","vm",f"nombre = '{vm}'")
        estado_vm=estado_vm[0]
        return estado_vm[0]

    def registrarDataCadaMinuto(self):
        conn = Conexion()
        server_names = ["Worker1","Worker2","Worker3","Worker4","Worker5","Worker6",
                        "Compute1","Compute2","Compute3","Compute4","Compute5","Compute6"]
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        try:
            with conn.cursor() as cur:
                validador = Validador()
                schedule.every(1).minutes.do(validador.registerAllData(server_names),cur=cur,conn=conn,timestamp=timestamp)
                while True:
                    schedule.run_pending()
                    time.sleep(1)
        finally:
            conn.close()

    def obtenerDataActual(self):
        url = 'http://10.20.12.58:8081/cpu-metrics'
        data_actual = requests.get(url)
        #datos = [ram]
        #header = {'accept': 'application/json'}
        return data_actual.json()

    def registerData(self,nombre):
        validador = Validador()
        conn = Conexion()
        #nombre = "headnode"
        id = conn.Select("recursos_id_estado","servidor",f"nombre = '{nombre}'")
        data = conn.Select("ram,vcpu,storage","recursos",f"id_estado = {id}")
        data_actual = validador.obtenerDataActual()
        data_actual = data_actual[nombre]
        ram_actual = data_actual["ram"]
        vcpu_actual = data_actual["vcpu"]
        storage_actual = data_actual["storage"]
        #porcentajes
        #ram_actual = ((data[0]-ram_actual)/data[0])*100
        #vcpu_actual = ((data[1]-vcpu_actual)/data[1])*100
        #vcpu_actual = data[1]-vcpu_actual
        #storage_actual = ((data[2]-storage_actual)/data[2])*100
        #registrar
        conn.Insert("recursos","ram_available,vcpu_available,storage_available",f"{ram_actual},{vcpu_actual},{storage_actual}")
        pass

    def registerAllData(cur, server_names):
        validador = Validador()
        #server_names = [headnode,worker1,worker2]
        for i in server_names:
            validador.registerData(server_names[i])

