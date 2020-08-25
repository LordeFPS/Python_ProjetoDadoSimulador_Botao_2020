# Faz um Simulador de dado

# Exemplo de como gerar numeros inteiros aleatório
# import random
# dado = random.randint(1, 6)
# print(dado)


import random # importa uma biblioteca aleatoriedade

import os     # importa uma opção para limpar a tela

import time


while True:
    
    time.sleep(1) # aqi conseguimos fazer um temporizador de tela
    
    os.system('clear') # os.system('cls' if os.name == 'nt' else 'clear') # com esse código conseguimos limpar a tela

    print("Pressione ENTER!")
    input()

    print('''
    ---------------------------------------
    ------ Gerar um Numero aleatório ------
    ------      Escolha um dado      ------
    ------      (1) - Dado de 4      ------
    ------      (2) - Dado de 6      ------
    ------      (3) - Dado de 8      ------
    ------      (4) - Dado de 10     ------
    ------      (5) - Dado de 12     ------
    ------      (6) - Dado de 20     ------
    ------      (7) - Dado de 100    ------
    ------      (8) - Sair           ------
    ---------------------------------------
    ---------------------------------------
    '''
    )
        
    opcao = input()
    
    if opcao == '1':
        
        dado = random.randint(1 , 4)

        print(f"Valor: {dado}") # exibir com f-string
        

    elif opcao == '2':
        dado = random.randint(1 , 6)

        print(f"Valor: {dado}")
    elif opcao == '3':
        dado = random.randint(1 , 8)

        print(f"Valor: {dado}")
    elif opcao == '4':
        dado = random.randint(1 , 10)

        print(f"Valor: {dado}")
    elif opcao == '5':
        dado = random.randint(1 , 12)

        print(f"Valor: {dado}")
    elif opcao == '6':
        dado = random.randint(1 , 20)

        print(f"Valor: {dado}")
    elif opcao == '7':
        dado = random.randint(1 , 100)

        print(f"Valor: {dado}")
    elif opcao == '8':
        print("Obrigado usar nosso Programa!")
        break
    else:
        print("Opção Inválida!")
