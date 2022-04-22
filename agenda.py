import csv

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
            telefono = input('Ingrese su telefono: ')
            csvfile = open('lista_contactos.csv')
            contactos = list(csv.DictReader(csvfile))
            for contacto in contactos:
                if contacto['phone'] == telefono:
                    print('Nombre del Contacto:', contacto['nombre'])
                    print('Numero de telefono:', contacto['phone'])
                    break
            csvfile.close()

        elif opcion == 2:
            
            nuevo_contacto = {}
            nuevo_contacto['phone'] = input('Ingrese su telefono: ')
            nuevo_contacto['nombre'] = input('Ingrese su nombre: ')

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

        elif opcion == 3:
            telefono = input('Ingrese su telefono: ')
            csvfile = open('lista_contactos.csv')
            contactos = list(csv.DictReader(csvfile))
            for contacto in contactos:
                if contacto['phone'] == telefono:
                    telefono_modificado = input('Ingrese el nuevo numero: ')
                    contacto['phone'] = telefono_modificado
                    print('Modificado')
                    break
            csvfile.close()

    print('Hasta la proxima.')
