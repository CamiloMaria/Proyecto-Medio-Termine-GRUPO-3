from Paises import Countries

paises = Countries()

menu='''\n                                  
1) Insertar País      
2) Eliminar País       
3) Modificar País      
4) Imprimir Paises    
5) Salir'''

def main():

    opcion='0'

    while opcion !='5':
        print(menu)
        opcion = input("¿Que opción deseas?")
        
        if opcion == '1':
            print("*Eligio Insertar Paises*")

            ISO3 = input("Introduce la clave ISO3 del nuevo País: ")
            CountryName = input("Introduce el nombre del nuevo País: ")
            Capital = input("Introduce la capital del nuevo País: ")
            CurrencyCode = input("Introduce el código de su moneda: ")

            r = paises.insertar_pais(ISO3,CountryName,Capital,CurrencyCode)
            
            if(r==0):
                print("-> No se pudo insertar el páis...")
            else:
                print("-> El páis se insertó correctamente")
        elif opcion == '2':
            print("*****  Eliminar Paises  *****")
            Id = int(input("Introduce el Id del país que desea eliminar: "))
            r = paises.eliminar_pais(Id)
            if(r==0):
                print("-> El páis no existe")
            else:
                print("-> El páis se eliminó correctamente")
        elif opcion == '3':
            print("*****  Modificar Paises  *****")
            Id = int(input("Introduce el Id del país que desea modificar: "))
            pais = paises.buscar_pais(Id)
            if pais == None:
                print("-> El páis no existe")
            else:
                print("*** Pais a modificar: ")
                print(pais)
                print()
                ISO3 = input("Introduce la nueva clave ISO3 del  País: ")
                CountryName = input("Introduce el nuevo nombre del  País: ")
                Capital = input("Introduce la nueva capital del  País: ")
                CurrencyCode = input("Introduce el nuevo código de su moneda: ")
                r = paises.modificar_pais(Id,ISO3,CountryName,Capital,CurrencyCode)
                if(r==0):
                    print("-> Error al modificar el país...")
                else:
                    print("-> El páis se modificó correctamente")

        elif opcion == '4':
            print("*****  Imprimir Paises  *****")
            print(paises)
        elif opcion == '5':
            print("-> Saliendo del sistema")
        else:            
            print("-> Opción no válida")


    


if __name__ == "__main__":
    main()
