import os
import socket
from Paises import Paises

paises = Paises()

#Declarar la direccion y puerto de UDP
UDP_IP = "localhost"
UDP_PORT = 3005

menu='''\n                                  
1) Insertar País      
2) Eliminar País       
3) Modificar País      
4) Imprimir Paises    
5) Salir'''

def send_data(pais):
    # Crear un socket para enviar datos
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Convertir el objeto país a una cadena de texto
    pais_data = str(pais)

    # Enviar los datos del país al servidor UDP
    sock.sendto(pais_data.encode(), (UDP_IP, UDP_PORT))

def main():

    opcion='0'
    
    while opcion !='5':
        os.system('cls')    

        print(menu)
        opcion = input("Elige una opcion: ")

        os.system('cls')

        if opcion == '1':
            print("\n*Eligio Insertar Paises*\n")

            
            ISO3 = input("Introduce la clave ISO3 del nuevo País: ")
            CountryName = input("Introduce el nombre del nuevo País: ")
            Capital = input("Introduce la capital del nuevo País: ")
            CurrencyCode = input("Introduce el código de su moneda: ")

            r = paises.insertar_pais(ISO3,CountryName,Capital,CurrencyCode)

            if(r==0):
                print("-> No se pudo insertar el páis...")
            else:
                print("-> El páis se insertó correctamente")
                #Envia los datos al servidor UDP
                send_data(r) 
             
        elif opcion == '2':
            print("\n*Eliminar Paises*\n")

            Id = int(input("Introduce el Id del país que desea eliminar: "))
            r = paises.eliminar_pais(Id)

            if(r==0):
                print("-> El páis no existe")
            else:
                print("-> El páis se eliminó correctamente")
                #Envia los datos al servidor UDP
                send_data(r)


        elif opcion == '3':
            print("\n*Modificar Paises*\n")

            Id = int(input("Introduce el Id del país que desea modificar: "))
            pais = paises.buscar_pais(Id)

            if pais == None:
                print("-> El páis no existe")
            else:
                print("Pais a modificar: ")
                print(pais)

                ISO3 = input("Introduce la nueva clave ISO3 del  País: ")
                CountryName = input("Introduce el nuevo nombre del  País: ")
                Capital = input("Introduce la nueva capital del  País: ")
                CurrencyCode = input("Introduce el nuevo código de su moneda: ")

                r = paises.modificar_pais(Id,ISO3,CountryName,Capital,CurrencyCode)

                if(r==0):
                    print("-> Error al modificar el país...")
                else:
                    print("-> El páis se modificó correctamente")
                    #Envia los datos al servidor UDP
                    send_data(pais)

        elif opcion == '4':
            print("\n*Imprimir Paises*\n")
            print(paises)
            os.system('pause')   

        elif opcion == '5':
            print("Cerrando...")

        else:            
            print("Opcion no valida")

if __name__ == "__main__":
    main()