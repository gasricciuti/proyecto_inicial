import csv

if __name__ == "__main__":
    print('AGENDA DE CONTACTOS')

    opcion = 0

    while opcion != '5': # while opcion != '5', donde 5 es la opcion para salir de mi ciclo
        print()
        print('AGENDA DE CONTACOS')
        print('******************')
        print('1. Consultar')
        print('2. Anadir')
        print('3. Modificar')
        print('4. Borrar')
        print('5. Salir')
        print('******************')

        opcion = input('Ingrese una opcion: ')

        if opcion == '1':
            # Generar lista de contactos a partir del archivo CSV (csvfile)
            # contactos = list(csv.DictReader(csvfile))
            # Utilizar for para recorrer la lista de contactos
            # ejemplo: for contacto in contactos:
            #               if contacto['phone'] == telefono
            #                   print(contacto)contacto['nombre']
            telefono = input('Ingrese su telefono: ')
            csvfile = open('lista_contactos.csv')
            contactos = list(csv.DictReader(csvfile))
            for contacto in contactos:
                if contacto['phone'] == telefono:
                    print('Nombre del Contacto:', contacto['nombre'])
                    print('Numero de telefono:', contacto['phone'])
            csvfile.close()

        elif opcion == '2':
            # nuevoContacto = {'phone': numero_telefono, 'nombre': nombre_contacto}
            # csvfile = open('lista_contactos.csv', 'w', newline='')
            # header = ['phone','nombre']
            # writer = csv.DictWriter(csvfile, fieldnames=header)
            # writer.writeheader()
            # writer.writerow(nuevoContacto)
            nuevo_contacto = {}
            nuevo_contacto['phone'] = input('Ingrese su telefono: ')
            nuevo_contacto['nombre'] = input('Ingrese su nombre: ')
            csvfile = open('lista_contactos.csv', 'a', newline='')
            headers = ['phone', 'nombre']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerow(nuevo_contacto)
            csvfile.close()
            print('El contacto fue añadido.')
            
        elif opcion == '3':            
            telefono = input('Ingrese su telefono: ')
            csvfile = open('lista_contactos.csv')
            contactos = list(csv.DictReader(csvfile))
            for contacto in contactos:
                if contacto['phone'] == telefono:
                    telefono_modificado = input('Ingrese el nuevo numero: ')
                    contacto['phone'] = telefono_modificado
                    print('Modificado')
            csvfile.close()

    else:
        print('Hasta la proxima.')

        
