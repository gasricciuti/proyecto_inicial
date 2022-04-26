import csv

csvfile = open('lista_contactos.csv')
contactos = list(csv.DictReader(csvfile))

def consultar():
    telefono = input('Ingrese su telefono: ')
    csvfile = open('lista_contactos.csv')
    contactos = list(csv.DictReader(csvfile))
    contador = 0
    for contacto in contactos:
        if contacto['phone'] == telefono:
            contador += 1
            print('Nombre del Contacto:', contacto['nombre'])
            print('Numero de telefono:', contacto['phone'])
    if contador == 0:
        print('Numero no existente')
            
def anadir():
    nuevo_contacto = {}
    nuevo_contacto['phone'] = input('Ingrese el telefono: ')
    nuevo_contacto['nombre'] = input('Ingrese el nombre: ')

    with open('lista_contactos.csv', 'r') as csvfile:
        file_has_data = csvfile.read(1)

    with open('lista_contactos.csv', 'a', newline='') as csvfile:
        headers = ['phone', 'nombre']
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        if not file_has_data:
            writer.writeheader()

        writer.writerow(nuevo_contacto)
        csvfile.close()
    print('El contacto fue añadido.')

def modificar():
    nuevo_contacto = {}
    numero_modificar = input('Ingrese el numero a modificar: ')
    contador = 0
    for numeros in contactos:
        if numeros['phone'] == numero_modificar:                                   
            contador += 1       
            nuevo_contacto['phone'] = input('Ingrese el nuevo numero: ')
            nuevo_contacto['nombre'] = input('Ingrese el nombre: ')
            with open('lista_contactos.csv', 'r') as csvfile:
                file_has_data = csvfile.read(1)

            with open('lista_contactos.csv', 'a', newline='') as csvfile:
                headers = ['phone', 'nombre']
                writer = csv.DictWriter(csvfile, fieldnames=headers)

                if not file_has_data:
                    writer.writeheader()

                writer.writerow(nuevo_contacto)
                csvfile.close()

            print('El contacto fue modificado')
    if contador == 0:
        print('Numero no existente')

def salir():
    print('SALIR')        


if __name__ == "__main__":
    print('AGENDA DE CONTACTOS')

    opcion = 0

    # Menu de la agenda con un bucle while.
    while opcion != 5:
        print()
        print('AGENDA DE CONTACOS')
        print('******************')
        print('1. Consultar')
        print('2. Anadir')
        print('3. Modificar')
        print('4. Borrar')
        print('5. Salir')
        print('******************')

        opcion = int(input('Ingrese una opcion: '))

        if opcion == 1:
            consultar()
        if opcion == 2:
            anadir() 
        if opcion == 3:
            modificar()
        if opcion == 4:
            borrar()
        if opcion == 5:
            salir()
