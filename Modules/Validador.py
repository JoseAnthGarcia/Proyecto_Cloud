import requests
import json
import pymysql
import schedule
import time
import datetime
from conf.Conexion import *

class Validador:
    def __init__(self):
        pass

    def validar_recursos(delf, recursos):
        ram = recursos[0]
        disco = recursos[1]
        cpu = recursos[2]
        pass

    def validar_estado_vm(delf, vm):

        pass

    def enviarData(self):
        pass

    def obtenerDataActual(self):
        url = 'http://10.20.12.136:8081/ram'
        data_actual = requests.get(url)
        #datos = [ram]
        #header = {'accept': 'application/json'}
        return data_actual.json()

    def registerData(self,nombre):
        conn = Conexion()
        #nombre = "headnode"
        id = conn.Select("recursos_id_estado","servidor",f"nombre = {nombre}")
        data = conn.Select("ram,vcpu,storage","recursos",f"id_estado = {id}")
        data_actual = validador.obtenerDataActual()
        data_actual = data_actual[nombre]
        #porcentajes
        ram_actual = (data_actual[0]/data[0])*100
        vcpu_actual = (data_actual[1]/data[1])*100
        storage_actual = (data_actual[2]/data[2])*100
        #registrar
        conn.Insert("recursos","ram_available,vcpu_available,storage_available",f"{ram_actual},{vcpu_actual},{storage_actual}")
        pass

    def registerAllData(cur, server_names):
        #server_names = [headnode,worker1,worker2]
        for i in server_names:
            validador.registerData(server_names[i])


validador = Validador()
server_names = ["headnode","worker1,worker2"]
validador.registerAllData(server_names)