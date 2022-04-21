

import csv

contactos = [{'phone': '1234', 'nombre': 'gaston'}]

with open('lista_contactos.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(contactos)

    for telf in contactos:
        print(telf['phone'])


if __name__ == "__main__":
    print('AGENDA DE CONTACTOS')

    menu = True

    while menu:
        print()
        print('AGENDA DE CONTACOS')
        print('******************')
        print('1. Consultar')
        print('2. Anadir')
        print('3. Modificar')
        print('4. Borrar')
        print('5. Salir')
        print('******************')

        opcion = ''
        while opcion not in ('1', '2', '3', '4, 5'):
            opcion = input('Ingrese una opcion: ')

            if opcion == '1':
                telefono = input('Ingresar telefono: ')
                if telefono not in telf['phone']:
                    print('Ese contacto no existe')
                else:
                    consultar = telf['nombre']
                    print('Contacto', consultar,
                          '\n''Telefono', telefono)

            elif opcion == '2':
                telefono = input('Ingresar telefono: ')
                if telefono in telf['phone']:
                    print('Ese telefono ya esta registrado')
                else:
                    nuevo = input('Ingrese su nombre y apellido: ')
                    telf['phone'] = telefono
                    telf['nombre'] = nuevo
                    print('Contacto nuevo agregado')

            elif opcion == '5':
                menu = False
                break
file.close()
