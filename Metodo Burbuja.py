def metodo_burbuja(lista_num):
    longuitud = len(lista_num) - 1

    for i in range(0, longuitud):
        for j in range(0, longuitud):
            if lista_num[j] > lista_num[j + 1]:
                aux = lista_num[j]
                lista_num[j] = lista_num[j + 1]
                lista_num[j + 1] = aux
    return lista_num


puntaje = [70, 90, 0, 80, 60, 85]
print('Antes de Ordenar: ')
print(puntaje)
print('Lista Ordenada: ')
print(metodo_burbuja(puntaje))
