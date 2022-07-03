import requests
import json
import pymysql
import schedule
import time
import datetime

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

    def obtener_data(self, bd):
        pass

    def registrar_data(self):
        ram = requests.get('http://10.20.12.136:8081/ram')
        datos = [ram]
        header = {'accept': 'application/json'}
        print(ram.json())
        conn = pymysql.connect(host='10.20.12.136', user='user', password='pass', db='db')
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        sql = ""
        try:
            with conn.cursor() as cur:
                #cur.execute(sql, (datos[0], datos[1], datos[2], datos[3], datos[4], timestamp))
                #conn.commit()
                #print(f"Guardando métricas de general_info")
                schedule.every(1).minutes.do(Validador.registerEveryMinute( cur=cur, conn=conn, timestamp=timestamp))
                while True:
                    stop = input("Pulse la tecla ’q’ para detener el guardado")
                    if stop == "q":
                        print("Se detuvo el registro")
                        break
                    schedule.run_pending()
                    time.sleep(1)

        finally:
            conn.close()
        pass

    def registerEveryMinute(cur, conn,data, timestamp):
        data = ""
        ram_data = ""
        sql_cpu = "Insert into recursos(vcpu,ram,storage,vcpu_available,ram_available,storage_available) values (%s,%s,%s,%s,%s,%s)"
        cur.execute(sql_cpu, (data[0], data[1], data[2], data[3], data[4],data[5]))
        conn.commit()
        print(f"Guardando métricas")


validador = Validador()
validador.registrar_data()