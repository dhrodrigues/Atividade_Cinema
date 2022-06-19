
#Inicio do Codigo
quantidade_assentos = int(input('Informe a quantidade de assentos: '))
assentos = ['-']*quantidade_assentos
local=0

#Dicionario que direciona as colunas de strings para inteiros
dicionario = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9,
    'j' : 10,
}


#Loop do cinemana.
while(local < len(assentos)):
    #Cabecario e inditificação das colunas
    print("\n\t\tBem-Vindo ao CineDH\n")
    letras_coluna = print('\nA B C D E F G H I J')
    NumeroFila = 1
    

    #Lugares
    for x in range(quantidade_assentos):
        
        print(assentos[x], end = " ")

        if ((x+1)%10 == 0):
            print(NumeroFila, '\n')
            NumeroFila+=1
    
        #Escolha dos lugares
        fila = int(input('\nDigite a fila desejada: '))
        coluna = input('Digite a coluna desejada: ')
        coluna = coluna.strip()

        lugarNoCinema = (fila-1)*10+(dicionario[coluna])

#Verificação dos lugares ocupados.
    if(assentos[lugarNoCinema-1] == 'x'):
        local-=1
        print('A CADEIRA ESTÁ OCUPADA! ESCOLHA OUTRO LUGAR: ')
    local+=1

#Finalização do Loop após todas as cadeiras estarem ocupadas.
    assentos[lugarNoCinema-1] = 'x'
print('\t\t-- CINEMA LOTADO -- \n\n A SESSÃO VAI COMEÇAR JÁ JÁ .. TENHA UM BOM FILME! \n')