import mysql.connector

class Paises:

    def __init__(self):
        self.cn = mysql.connector.connect(host="localhost", user="root", passwd="123", database="paises_proyecto")



    def __str__(self): 
        
        datos=self.consultar_paises() #Llama a esa consulta y lo guarda en esa variable.
        aux=""

        for row in datos:
            aux=aux + str(row) + "\n"

        return aux
    
    def consultar_paises(self): #consulta de todas los paises
        cur = self.cn.cursor()

        cur.execute("SELECT * FROM countries")
        datos = cur.fetchall()
        cur.close()    

        return datos

    def buscar_pais(self, Id):
        cur = self.cn.cursor()

        sql= "SELECT * FROM countries WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    

        return datos
    
    def insertar_pais(self,ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cn.cursor()

        sql='''INSERT INTO countries (ISO3, CountryName, Capital, CurrencyCode) 
        VALUES('{}', '{}', '{}', '{}')'''.format(ISO3, CountryName, Capital, CurrencyCode)
        cur.execute(sql)
        n=cur.rowcount
        self.cn.commit()    
        cur.close()

        return n    

    def eliminar_pais(self,Id):
        cur = self.cn.cursor()

        sql='''DELETE FROM countries WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cn.commit()    
        cur.close()

        return n   

    def modificar_pais(self,Id, ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cn.cursor()

        sql='''UPDATE countries SET ISO3='{}', CountryName='{}', Capital='{}',
        CurrencyCode='{}' WHERE Id={}'''.format(ISO3, CountryName, Capital, CurrencyCode,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cn.commit()   
        cur.close()

        return n   
