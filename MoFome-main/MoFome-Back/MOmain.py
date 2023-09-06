import os
from sistema import *

print("\n------")
print("MoFome")
print("------\n")

while True:
    try:
        print ("\nDigite 1 para criar uma conta.") 
        print ("Digite 2 logar na sua conta.")
        print ("Digite 3 para recuperar o seu ID.")
        print ("Digite 4 para recuperar o seu nome de usuário.")
        print ("Digite 20 para encerrar o programa.")


        action = input("\nInsira a opção: ")

        if action == '1':
            login.abrirConta()

        elif action == '2':
            checarSeEncerra = login.logarNaConta()
            if checarSeEncerra == False:
                break

        elif action == '3':
            login.recoverID()

        elif action == '4':
            login.accountRecovery()

        elif action == '20':
            break
        
        else:
            print('\nOpção Inválida. Por favor, insira uma opção válida')
            
    except Exception as e:
        print(f'Erro: {e}')