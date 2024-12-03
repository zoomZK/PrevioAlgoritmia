import random

def cargarLibros(lista):
    while len(lista) != 150:
        valor = random.randint(1000, 5000)
        if len(lista) == 0:
            lista.append(valor)
        elif len(lista) != 0:   
            if duplicado(lista, valor) == -1:
                lista.append(valor)
                ordenado(lista)         
    return

def duplicado(lista, dato):
    izq = 0
    der = len(lista) -1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            pos = centro
        elif lista[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
    return pos

def ordenado(lista):
    rango = len(lista)
    for i in range(rango - 1):
        for j in range (i + 1, rango):
            if lista[i]>lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return 

def registrarVotos(lista1, lista2):
    for i in range(len(lista1)):
        lista2.append(0)
    dato = int(input("Ingrese el codigo del libro que desea buscar: "))
    while dato != -1:
        codigo = duplicado(lista1, dato)
        if codigo != -1:
            voto = int(input("Ingrese el voto que desea darle: "))
            if voto >= 1 and voto <= 10:
                if lista2[codigo] == 0:
                    lista2[codigo] = voto
                else:
                    acumulador = lista2[codigo]
                    acumulador += voto
                    lista2[codigo] = acumulador
            else:
                print("Voto invalido")
        else:
            print("Codigo del libro no encontrado")
        dato = int(input("Ingrese el codigo del libro que desea buscar: "))

def mostrarVotacion(lista1, lista2):
    contador = 0
    print("VOTOS PARA LOS LIBROS")
    print("CODIGO              VOTOS")
    for i in range(len(lista1)):
        if lista2[i] > 0:
            print(lista1[i],"                ", lista2[i])
            contador += lista2[i]
    print("El total de votos fue de:", contador)
        

def librosSinVotos(lista1, lista2):
    aux = []
    print("SERIES SIN VOTOS")
    print("CODIGO              VOTOS")
    for i in range(len(lista2)):
        if lista2[i] == 0:
            print(lista1[i],"                ", lista2[i])
            aux.append(0)
    if len(aux) == 0:
        print("Todas las series recibieron votos")


def main():
    votos = []
    libros = []
    cargarLibros(libros)
    registrarVotos(libros, votos)
    mostrarVotacion(libros, votos)
    librosSinVotos(libros, votos)

if __name__=="__main__":
    main()
