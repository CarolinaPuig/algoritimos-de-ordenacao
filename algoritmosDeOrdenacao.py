##  Carolina Puig 
##  Guilherme Costa

def montarLista(tamanhoLista):
    import random
    lista=[]
    for i in range (tamanhoLista):
        lista.append(random.randint(1,(tamanhoLista)))
    return lista

def bubbleSort(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp

def selectionSort(lista):
    for i in range (len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
  
def insertionSort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j] :
                lista[j + 1] = lista[j]
                j -= 1
        lista[j + 1] = key
  
def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        L = lista[:meio]
        R = lista[meio:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i] <= R[j]:
                lista[k] = L[i]
                i+=1
            else:
                lista[k] = R[j]
                j+=1
            k+=1
        while i<len(L):
            lista[k]=L[i]
            i+=1
            k+=1
        while j < len(R):
            lista[k] = R[j]
            j+=1
            k+=1

def partition(lista, comeco, fim):
    pivot = lista[comeco]
    low = comeco + 1
    high = fim
    while True:
        while low <= high and lista[high] >= pivot:
            high = high - 1
        while low <= high and lista[low] <= pivot:
            low = low + 1
        if low <= high:
            lista[low], lista[high] = lista[high], lista[low]
        else:
            break
    lista[comeco], lista[high] = lista[high], lista[comeco]
    return high

def quickSort(lista, comeco, fim):
    if comeco >= fim:
        return
    p = partition(lista, comeco, fim)
    quickSort(lista, comeco, p-1)
    quickSort(lista, p+1, fim)


import time
def get_time(lista, menu): 
    tempo=0
    if menu == 1:   
        inicio = time.time()  
        bubbleSort(lista)
        fim = time.time()
        tempo=fim-inicio
    elif menu == 2:   
        inicio = time.time()  
        selectionSort(lista)
        fim = time.time()
        tempo=fim-inicio
    elif menu == 3:   
        inicio = time.time()  
        insertionSort(lista)
        fim = time.time()
        tempo=fim-inicio
    elif menu == 4:   
        inicio = time.time()  
        mergeSort(lista)
        fim = time.time()
        tempo=fim-inicio
    elif menu==5:
        inicio = time.time()  
        quickSort(lista, 0, len(lista) - 1)
        fim = time.time()
        tempo=fim-inicio
    return tempo


def menuPrincipal():
    menu = int(input("Escolha um algoritmos de ordenação\n1.Bubble Sort\n2.Selection Sort\n3.Insertion Sort\n4.Merge Sort\n5.Quick Sort\n"))
    while menu not in [1,2,3,4,5]:
        menu = int(input("Opção inválida! \nEscolha um algoritmos de ordenação\n1.Bubble Sort\n2.Selection Sort\n3.Insertion Sort\n4.Merge Sort\n5.Quick Sort\n--> "))
    return menu


def nomeAlgoritmo(menu):
    if menu==1:
        nomeAlgoritmo='\t\t   Algoritmo: Bubble Sort\n'
    elif menu==2:
        nomeAlgoritmo='\t\t   Algoritmo: Selection Sort\n'
    elif menu==3:
        nomeAlgoritmo='\t\t   Algoritmo: Insertion Sort\n'
    elif menu==4:
        nomeAlgoritmo='\t\t   Algoritmo: Merge Sort\n'
    elif menu==5:
        nomeAlgoritmo='\t\t   Algoritmo: Quick Sort\n'
    return nomeAlgoritmo


#Principal:
medias=[]
menu = menuPrincipal()
print(f'--------------- Médias de tempo das execuções: ---------------\n')
print(nomeAlgoritmo(menu))
tempoTotal=0
for i in range(20):
    tempo=get_time(montarLista(1000), menu)
    print(f'{tempo:.3f}')  
    tempoTotal+=tempo
media=tempoTotal/20
medias.append(f'{media:.3f}')
print(f'Lista com 1000 elementos: {media:.3f} segundos\t {(media/60):.2f} minutos')
tempoTotal=0
for i in range(20):
    tempo=get_time(montarLista(5000), menu)
    print(f'{tempo:.3f}')    
    tempoTotal+=tempo
media=tempoTotal/20
medias.append(f'{media:.3f}')
print(f'Lista com 5000 elementos: {media:.3f} segundos\t {(media/60):.2f} minutos')
tempoTotal=0
for i in range(20):
    tempo=get_time(montarLista(10000), menu)
    print(f'{tempo:.3f}')    
    tempoTotal+=tempo
media=tempoTotal/20
medias.append(f'{media:.3f}')
print(f'Lista com 10000 elementos: {media:.3f} segundos\t {(media/60):.2f} minutos')
tempoTotal=0
for i in range(20):
    tempo=get_time(montarLista(20000), menu)
    print(f'{tempo:.3f}')    
    tempoTotal+=tempo
media=tempoTotal/20
medias.append(f'{media:.3f}')
print(f'Lista com 20000 elementos: {media:.3f} segundos\t {(media/60):.2f} minutos')
tempoTotal=0
for i in range(20):
    tempo=get_time(montarLista(50000),menu)
    print(f'{tempo:.3f}')    
    tempoTotal+=tempo
media=tempoTotal/20
medias.append(f'{media:.3f}')
print(f'Lista com 50000 elementos: {media:.3f} segundos\t {(media/60):.2f} minutos')
print(medias)

