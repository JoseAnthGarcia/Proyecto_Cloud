import pymysql

class Conexion:

    def __init__(self):
        pass

    def conectar(self):
        ip=""
        username=""
        paswd=""
        database=""
        con = pymysql.connect(host=ip,user= username,password=paswd, db=database)
        return con

    def Select(self,valores,tabla,condicion):
        con=self.conectar()
        resultado=0
        try:
            with con.cursor() as cur:
                if condicion=="-1":
                    cur.execute("Select "+valores+" from " +tabla+ " where "+condicion)
                else:
                    cur.execute("Select "+valores+" from "+tabla)
                resultado = cur.fetchall()
        finally:
            con.close()
        return resultado

    def Insert(self,tabla,columna,valores):
        con=self.conectar()
        try:
            with con.cursor() as cur:
                #columna separadas por comas (,)
                #valores separados por comas (,)
                cur.execute("Insert into "+tabla+"("+columna+")"+" values ("+valores+")")
                con.commit()
        finally:
            con.close()
    
    def Update(self,tabla,valores,condicion):
        con=self.conectar()
        try:
            with con.cursor() as cur:
                #valores separados por comas (,)
                cur.execute("Update "+tabla+" set "+valores+"where "+condicion)
                con.commit()
        finally:
            con.close()
    def Consult(self,query):
        con=self.conectar()
        resultado=0
        try:
            with con.cursor() as cur:
                cur.execute(query)
                resultado = cur.fetchall()
        finally:
            con.close()
        return resultado