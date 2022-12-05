from connect import cn

class Countries:

    def __init__(self):
        cn

    def __str__(self): 
        datos=self.consultar_paises() #Llama a esa consulta y lo guarda en esa variable.
        aux=""

        for row in datos:
            aux=aux + str(row) + "\n"

        return aux
    
    def consultar_paises(self): #consulta de todas los paises
        cur = self.cnn.cursor()

        cur.execute("SELECT * FROM countries")
        datos = cur.fetchall()
        cur.close()    

        return datos

    def buscar_pais(self, Id):
        cur = self.cnn.cursor()

        sql= "SELECT * FROM countries WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    

        return datos
    
    def insertar_pais(self,ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor()

        sql='''INSERT INTO countries (ISO3, CountryName, Capital, CurrencyCode) 
        VALUES('{}', '{}', '{}', '{}')'''.format(ISO3, CountryName, Capital, CurrencyCode)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()

        return n    

    def eliminar_pais(self,Id):
        cur = self.cnn.cursor()

        sql='''DELETE FROM countries WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()

        return n   

    def modificar_pais(self,Id, ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor()

        sql='''UPDATE countries SET ISO3='{}', CountryName='{}', Capital='{}',
        CurrencyCode='{}' WHERE Id={}'''.format(ISO3, CountryName, Capital, CurrencyCode,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()   
        cur.close()

        return n   
