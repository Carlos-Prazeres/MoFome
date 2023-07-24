from datetime import datetime
import os

accountsList = []
managementList = {}
lista_de_arquivos_de_receitas_e_topicos = []
lista_de_ids_receitas = []
lista_de_ids_topicos = []
lista_de_nomes_de_usuarios = []
data_e_hora = datetime.now()
data = data_e_hora.strftime('%d/%m/%Y %H:%M')



def newAccount(aName, aPassword, aUser):
    global accountsList
    friendList = []
    receitas = 0
    receitas_avaliadas = []
    comentarios = []
    comentario = []
    topicos = 0
    privacidade = 0
    ids_amigos = []
    newAccountDict = {'nome':aName, 'senha':aPassword, 'user':aUser, 'friends' :friendList, 'id_da_receita' :receitas, 'receitas_avaliadas': receitas_avaliadas, 'comentarios_nas_receitas': comentarios,  'id_topicos': topicos, 'comentarios_nos_topicos': comentario, 'modo_de_privacidade': privacidade, 'lista_ids_dos_amigos': ids_amigos} 
    accountsList.append(newAccountDict)



def show(accountNumber):
    global accountsList
    print('Conta', accountNumber)

    thisAccountDict = accountsList[int(accountNumber)]

    #print('     Nome:', thisAccountDict['nome'])
    print('     Senha:', thisAccountDict['senha'])
    print('     Nome de Usuário:', thisAccountDict['user'])
    friendList = thisAccountDict['friends']
    print ("       Seguindo:")
    for i in range (len(friendList)):
        print ('              ' + friendList[i])
    print()



def accountRecovery(accountNumber):
    global accountsList
    thisAccountDict = accountsList[int(accountNumber)]
    print('Seu nome de usuário é:', thisAccountDict['user'])
    print('Sua senha é:', thisAccountDict['senha'])



def changeProfile(newPassword, newUser, accountNumber):
    global accountsList
    thisAccountDict = accountsList[int(accountNumber)]
    thisAccountDict['senha'] = newPassword
    thisAccountDict['user'] = newUser


def topicos(accountNumber):
    global accountsList
    global lista_de_arquivos_de_receitas_e_topicos
    global lista_de_ids_topicos
    
    thisAccountDict = accountsList[int(accountNumber)]

    thisAccountDict['id_topicos'] = int(thisAccountDict['id_topicos']) + 1

    id_topico = thisAccountDict['id_topicos']

    filename = f"Topico_{id_topico}_{thisAccountDict['user']}.txt"

    id = f"{id_topico}{accountNumber}"
    
    lista_de_arquivos_de_receitas_e_topicos.append(filename)
    lista_de_ids_topicos.append(id)

    with open(filename, "w", encoding = "utf8") as file:
        if True:
            file.write(f"Este tópico foi criado pelo usuário {thisAccountDict['user'].capitalize()}\n\n")
            tema_do_topico = input("Insira o tema do tópico:\n")
            file.writelines(f"Tema do tópico: {tema_do_topico}\n\nRespostas:\n\n")
    print("Seu tópico foi postado\n")

    

def adicionar_comentario_topico(accountNumber):
    global accountsList
    lista_de_amigos = []
    amigo = False

    topico_existe = False
    id_aceitavel = False 
                                 
    thisAccountDict = accountsList[int(accountNumber)]

    lista_de_amigos = thisAccountDict['lista_ids_dos_amigos']

    while id_aceitavel == False:
        id_comentarista = input("Insira o seu ID:\n")

        if id_comentarista == 'r':     
            RecoverID()
        elif id_comentarista == 'end':      
            quit()                                                                                                                 
        elif id_comentarista.isdigit() == False or  int(id_comentarista) < 0 or int(id_comentarista) > int(len(accountsList) - 1):  
            print("Insira um id válido. Caso não se lembre do id, digite 'r' para recuperar o seu id ou 'end' para encerrar o programa\n")
        elif int(id_comentarista) >= 0 and int(id_comentarista) <= int(len(accountsList) - 1) and id_comentarista.isdigit() == True: 
            id_aceitavel = True

    if thisAccountDict['modo_de_privacidade'] == 1:
        for i in range(len(lista_de_amigos)):
            if id_comentarista == lista_de_amigos[i]:
                amigo = True
        if amigo == False:
            print("Esse usuário está com o modo de privacidade ativo. Apenas amigos podem comentar nos tópicos.\n\n")
            return
        

    id_aceitavel = False       

    while id_aceitavel == False:
        id_topico = input("Insira o ID do tópico:\n")

        if id_topico == 'retornar':
            return
        elif id_topico.isdigit() == False or  int(id_topico) < 0 or int(id_topico) > int(thisAccountDict['id_topicos']): 
           print("Insira um id válido. Caso não se lembre do id, digite 'retornar' para inserir outra opção\n")
        elif int(id_topico) >= 0 and int(id_topico) <= int(thisAccountDict['id_topicos']) and id_topico.isdigit() == True:
            id_aceitavel = True

    id = f"{id_topico}{accountNumber}"

    for i in range(len(lista_de_ids_topicos)):
        if id == lista_de_ids_topicos[i]:
            topico_existe = True

    if topico_existe == False:
        print("Esse tópico não existe\n")
        return
   

    arquivo_receita = f"Topico_{id_topico}_{thisAccountDict['user']}.txt"   

    thisAccountDict = accountsList[int(id_comentarista)] 
    
   
    with open(arquivo_receita, "a", encoding = "utf8") as file: 
        if True:
            comentario = input("Insira uma resposta\n")
            file.write(f"{thisAccountDict['user'].capitalize()} ({data}): {comentario}\n")
            thisAccountDict['comentarios_nos_topicos'].append(comentario)  



def postManagement(accountNumber):
    global accountsList
    global managementList
    global lista_de_arquivos_de_receitas_e_topicos
    avaliacoes = 0
    soma_de_notas = 0
    nota_media = 0
    
    thisAccountDict = accountsList[int(accountNumber)]

    thisAccountDict['id_da_receita'] = int(thisAccountDict['id_da_receita']) + 1

    id_receita = thisAccountDict['id_da_receita']

    filename = f"Receita_{id_receita}_{thisAccountDict['user']}.txt"

    id = f"{id_receita}{accountNumber}"

    lista_de_arquivos_de_receitas_e_topicos.append(filename)

    lista_de_ids_receitas.append(id)

    newManagementDict = {'soma_de_avaliacoes': avaliacoes, 'nota_media': nota_media, 'soma_de_notas': soma_de_notas}  #Cria o dicionar dessa receita. Cada uma precisa para saber as avaliações que ela recebe

    managementList[int(id)] = newManagementDict

    with open(filename, "w", encoding = "utf8") as file:
        if True:
            file.write(f"Esta receita foi postada pelo usuário {thisAccountDict['user'].capitalize()}\n\n\nAvaliação média da receita: %.1f\n\nReceita:\n\n" % nota_media)
            ingredientes = input("Escreva os ingredientes:\n")
            file.writelines(f"Ingredientes: {ingredientes}\n\n")
            modo_de_preparo = input("Escreva o modo de preparo:\n")
            file.writelines(f"Modo de preparo: {modo_de_preparo}\n\n")
            file.write("Comentários:\n\n")
    print('Sua receita foi criada')
    print(f"O ID da receita é: {thisAccountDict['id_da_receita']}\n")



def addFriends(accountNumber):
    global accountsList

    newFriend = input("Digite o id de quem você deseja adicionar:\n")

    while newFriend.isdigit() == False or  int(newFriend) < 0 or int(newFriend) > int(len(accountsList) - 1):
                print("Insira um id válido. Caso não se lembre do id, digite 'end' para encerrar o programa")
                newFriend = input("Insira o id do usuário que postou a receita:\n")
                if newFriend == 'end':
                    quit()


    thisAccountDict = accountsList[int(accountNumber)]
    friendAccountDict = accountsList[int(newFriend)]

    thisAccountDict['friends'].append(friendAccountDict['user'])
    thisAccountDict['lista_ids_dos_amigos'].append(accountNumber)
    thisAccountDict['lista_ids_dos_amigos'].append(newFriend)



def addComment(accountNumber):
    global accountsList
    global data
    global lista_de_ids_receitas # Utilizada para saber se a receita em que o usuário quer comentar existe.
    lista_de_amigos = []
    amigo = False
    receita_existe = False
    id_aceitavel = False 
                                  #utilizada para verificação do ID da receita e do usuário que está comentando.
    thisAccountDict = accountsList[int(accountNumber)]

    lista_de_amigos = thisAccountDict['lista_ids_dos_amigos']


    verificacao = thisAccountDict['id_da_receita']

    if verificacao == 0:
        print("Esse usuário não tem receitas postadas.\n")
        return

    while id_aceitavel == False:
        id_comentarista = input("Insira o seu ID:\n")

        if id_comentarista == 'r':      #recuperar ID.
            RecoverID()
        elif id_comentarista == 'end':      # encerrar o programa.
            quit()                                                                                                                 
        elif id_comentarista.isdigit() == False or  int(id_comentarista) < 0 or int(id_comentarista) > int(len(accountsList) - 1):  #Saber se o ID é um número, se é menor que 0 e se é maior que a quantidade de contas - 1.
            print("Insira um id válido. Caso não se lembre do id, digite 'r' para recuperar o seu id ou 'end' para encerrar o programa\n")
        elif int(id_comentarista) >= 0 and int(id_comentarista) <= int(len(accountsList) - 1) and id_comentarista.isdigit() == True: # Se passou nas outras condições, a variavel id_aceitavel se torna TRUE e quebra o while.
            id_aceitavel = True

    if thisAccountDict['modo_de_privacidade'] == 1:
        for i in range(len(lista_de_amigos)):
            if id_comentarista == lista_de_amigos[i]:
                amigo = True
        if amigo == False:
            print("Esse usuário está com o modo de privacidade ativo. Apenas amigos podem comentar nas receitas.\n\n")
            return
    

    id_aceitavel = False         #Volta a ser False para validar o id_receita.

    while id_aceitavel == False:
        id_receita = input("Insira o ID da receita:\n")

        if id_receita == 'retornar':
            return
        elif id_receita.isdigit() == False or  int(id_receita) < 0 or int(id_receita) > int(thisAccountDict['id_da_receita']): #Saber se o ID é um número, se é menor que 0 ou se é maior que a quantidade de receitas desse usuario.
           print("Insira um id válido. Caso não se lembre do id, digite 'retornar' para inserir outra opção\n")
        elif int(id_receita) >= 0 and int(id_receita) <= int(thisAccountDict['id_da_receita']) and id_receita.isdigit() == True:
            id_aceitavel = True

    id = f"{id_receita}{accountNumber}"

     

    for i in range(len(lista_de_ids_receitas)):
        if id == lista_de_ids_receitas[i]:
            receita_existe = True

    if receita_existe == False:
        print("Essa receita não existe\n")
        return
    
    arquivo_receita = f"Receita_{id_receita}_{thisAccountDict['user']}.txt"   #O arquivo é criado

    thisAccountDict = accountsList[int(id_comentarista)] #Agora pega o dicionario do usuario que está comentando, antes era o dicionário do usuário que fez a receita.
    
   
    with open(arquivo_receita, "a", encoding = "utf8") as file:  #adicionar um comentário ao arquivo txt dessa receita.
        if True:
            comentario = input("Insira um comentário\n")
            file.write(f"{thisAccountDict['user'].capitalize()} ({data}): {comentario}\n")
            thisAccountDict['comentarios_nas_receitas'].append(comentario)  #adiciona os comentários feitos por esse usuário a uma lista que está no seu dicionário. Será útil se ele escolher deletar todos os comentários(Opção 10).

    print("Comentário postado")


def addAvaliation(accountNumber):
    global accountsList
    global managementList
    global lista_de_ids_receitas
    lista_de_amigos = []
    amigo = False
    receita_existe = False
    avaliacao_aceitavel = False     #utilizada para verificação da nota da avaliação.
    id_aceitavel = False            #utilizada para verificação do ID do avaliador e do ID da receita.

    thisAccountDict = accountsList[int(accountNumber)]  # Dicionário do usuário que postou a receita.

    lista_de_amigos = thisAccountDict['lista_ids_dos_amigos']

    while id_aceitavel == False:
        id_avaliador = input("Insira o seu ID:\n")

        if id_avaliador == accountNumber:
            print("Você não pode avaliar a sua própria receita\n")
            return
        elif id_avaliador == 'r':                       
            RecoverID()
        elif id_avaliador == 'end':                      
            quit()
        elif id_avaliador.isdigit() == False or  int(id_avaliador) < 0 or int(id_avaliador) > int(len(accountsList) - 1):
            print("Insira um id válido. Caso não se lembre do id, digite 'r' para recuperar o seu id ou 'end' para encerrar o programa\n")
        elif int(id_avaliador) >= 0 and int(id_avaliador) <= int(len(accountsList) - 1) and id_avaliador.isdigit() == True:
            id_aceitavel = True

    if thisAccountDict['modo_de_privacidade'] == 1:
        for i in range(len(lista_de_amigos)):
            if id_avaliador == lista_de_amigos[i]:
                amigo = True
        if amigo == False:
            print("Esse usuário está com o modo de privacidade ativo. Apenas amigos podem comentar nas receitas.\n\n")
            return

    id_aceitavel = False        #Volta a ser False para validar o id_receita.

    while id_aceitavel == False:
        id_receita = input("Insira o ID da receita:\n")

        if id_receita == 'retornar':
            return
        elif id_receita.isdigit() == False or  int(id_receita) < 0 or int(id_receita) > int(thisAccountDict['id_da_receita']):
           print("Insira um id válido. Caso não se lembre do id, digite 'retornar' para inserir outra opção\n")
        elif int(id_receita) >= 0 and int(id_receita) <= int(thisAccountDict['id_da_receita']) and id_receita.isdigit() == True:
            id_aceitavel = True                                         # Concatenação do id_da_receita e do usuario que postou a receita.
                                            # Exemplo: Usuário de ID 0 postou receita e o id_receita escolhido foi 2. A variavel ID se torna uma string 02.
    id = f"{id_receita}{accountNumber}"     # É necessário para adicionar as receitas avaliadas a uma lista que fica no dicionário do usuário que está avaliando.
                                            # Também é necessário para pegar o dicionario de receitas

    for i in range(len(lista_de_ids_receitas)): # Verificar se a receita existe. 
        if id == lista_de_ids_receitas[i]:
            receita_existe = True

    if receita_existe == False:
        print("Essa receita não existe\n")
        return 

    arquivo_receita = f"Receita_{id_receita}_{thisAccountDict['user']}.txt"   # O arquivo que ele quer avaliar.

    thisAccountDict = accountsList[int(id_avaliador)]   #Pega o dicionário do usuário que está avaliando.

    receitas_avaliadas = thisAccountDict['receitas_avaliadas']   # Passa a lista para uma outra variavel
  
    #verifica se ele já avaliou essa receita. Percorre toda a lista procurando o id(concatenação), se ele achar, mostra a mensagem abaixo e faz o usuário escolher outra opção.

    for i in range(len(receitas_avaliadas)):    
        if id == receitas_avaliadas[i]:               
            print("Você já avaliou essa receita. Escolha outra opção:\n")
            return
        

    #verifica se o valor que ele recebe na variavel avaliacao pode ser aceito
    while avaliacao_aceitavel == False:
        avaliacao = input("Avalie a receita com uma nota de 0 a 5:\n")
        if avaliacao.isdigit() == False or int(avaliacao) < 0 or int(avaliacao) > 5:
            print("Só é possível inserir uma nota de 0 a 5:\n")
        else:
            avaliacao_aceitavel = True

    thisAccountDict['receitas_avaliadas'].append(id)   #Adiciona o ID concatenado a lista de receitas avaliadas por esse usuário.


    managementDict = managementList[int(id)]    # Agora pega o dicionario do id concatenado dessa receita.

    nota_media = managementDict['nota_media']   # Passa a nota media para uma variavel nota_media para saber o texto antigo (É necessário para fazer a substituição no arquivo).

    texto_antigo = (f"Avaliação média da receita: %.1f" % nota_media)


    managementDict['soma_de_avaliacoes'] = managementDict['soma_de_avaliacoes'] + 1  # Mais um usuário avaliou essa receita.
    managementDict['soma_de_notas'] = managementDict['soma_de_notas'] + int(avaliacao)  # Soma a nota que o usuário colocou nessa função com as outras notas.
    managementDict['nota_media'] =  managementDict['soma_de_notas'] / managementDict['soma_de_avaliacoes']  # Calcula a nota_media.

    nota_media = managementDict['nota_media']  # Passa a NOVA nota_media para uma variável nota_media para colocar o texto_novo.

    texto_novo = (f"Avaliação média da receita: %.1f" % nota_media) # Texto novo que substituirá o texto antigo.
         

    substituir_texto_arquivo(arquivo_receita, texto_antigo, texto_novo)  # A função de substituir texto é chamada.

def privacidade(accountNumber):
    global accountsList

    thisAccountDict = accountsList[int(accountNumber)]
    
    thisAccountDict['modo_de_privacidade'] = 1

    print("Modo de privacidade ativado.\n")

def privacidade_desativar(accountNumber):
    global accountsList

    thisAccountDict = accountsList[int(accountNumber)]

    thisAccountDict['modo_de_privacidade'] = 0

    print("Modo de privacidade desativado.")
        


def RecoverID():
    global accountsList
    achou = False
    quantidade_de_usuarios = int(len(accountsList))

    username = input("Insira seu nome de usuário: ")

    senha = input("Insira sua senha: ")

    for i in range(quantidade_de_usuarios):
        thisAccountDict = accountsList[i]

    #verifica qual é a conta em que a senha e o nome de usuário são iguais a senha e o nome e usuário que o usuário que está tentando recuperar o ID colocou.       
        if username == thisAccountDict['user'] and senha == thisAccountDict['senha']:
            print(f"Seu id é {i}")
            achou = True
            break
        else:
            achou = False
    if achou == False:
        print("\nO nome de usuário e/ou a senha podem estar incorretos.\n")



def substituir_texto_arquivo(nome_arquivo, texto_antigo, texto_novo):   #substituir arquivos

    with open(nome_arquivo, 'r', encoding = "utf8") as file:  # Lê o conteúdo do arquivo.
        conteudo = file.read()

    # Substitui o texto do conteúdo.
    
    conteudo_modificado = conteudo.replace(f"{texto_antigo}", f"{texto_novo}")   
   

    # Reescreve o arquivo com as alterações.

    with open(nome_arquivo, 'w', encoding = "utf8") as file:
        file.writelines(f"{conteudo_modificado}")



def remover_comentario_arquivo(nome_arquivo, texto):

    with open(nome_arquivo, 'r', encoding = "utf8") as file:        # Lê o conteúdo do arquivo.
        conteudo = file.read()

    # Substitui o texto por uma string vazia. Quase o mesmo que remover.

    conteudo_modificado = conteudo.replace(f"{texto}", '')

    # Reescreve o arquivo com as alterações.

    with open(nome_arquivo, 'w', encoding = "utf8") as file:
        file.writelines(conteudo_modificado)


print("\n----------------------------")
print ("Olá, Bem Vindo(a) ao MoFome.")
print("----------------------------\n")

while True:
    print ("Digite 1 para criar uma conta.") #newAccount
    print ("Digite 2 para editar a sua conta.") #changeProfile
    print ("Digite 3 para adicionar pessoas para seguir.")
    print ("Digite 4 para postar uma receita.") #postmanagement
    print ("Digite 5 para recuperar a sua conta.") #accountRecovery
    print ("Digite 6 para adicionar um comentário à uma receita.")
    print ("Digite 7 para ver o seu perfil.") #show
    print ("Digite 8 para avaliar uma receita.")
    #print ("Digite 8 para ver o seu feed.") 
    print ("Digite 9 para sair.")
    print ("Digite 10 para deletar todos os seus comentários, receitas e tópicos. Não será possível recuperá-los.")
    print ("Digite 11 para criar um tópico de discussão.")
    print ("Digite 12 para adicionar uma resposta a um tópico de discussão.")
    print ("Digite 13 para ativar o modo de privacidade (apenas amigos podem avaliar e comentar nas suas receitas ou tópicos).")
    print ("Digite 14 para desativar o  modo de privacidade (todos podem avaliar e comentar nas suas receitas ou tópicos).")
    quantidade_de_usuarios = int(len(accountsList))
    if quantidade_de_usuarios >= 1:
        print ("Digite 15 para recuperar o seu id")

    action = input("Qual é a sua opcao?\n")

    if action == '1':
        usuarios = []
        new_name = input ("Qual o seu Nome?\n")
        new_name = new_name.lower()
        new_password = input ("Qual será a sua senha?\n")
        new_user = input ("Digite um nome de usuário:\n")
        
        
        if quantidade_de_usuarios >= 1:
            for i in range(len(accountsList)):
                while new_user == lista_de_nomes_de_usuarios[i]:
                    print("Esse nome de usuário já existe. Insira outro.\n")
                    new_user = input("Digite um nome de usuário:\n")

            
        lista_de_nomes_de_usuarios.append(new_user)

        new_user = new_user.lower()
        newAccount(newAccount, new_password, new_user )
        accountNumber = int (len(accountsList) - 1)
        print ('Seu id é o número', accountNumber)
        print ("Conta Criada\n")


    if action == '2':
        user = input ("Digite sua novo nome:\n")
        password = input ("Digite seu nova senha:\n")
        id_user = input ("Digite seu id:\n")
 
        while id_user.isdigit() == False or  int(id_user) < 0 or int(id_user) > int(len(accountsList) - 1):
            print("Insira um id válido. Caso não se lembre do id, digite 'r' para recuperar o seu id ou 'end' para encerrar o programa")
            id_user = input("Digite seu id:\n")
            if id_user == 'end':
                quit()
            if id_user == 'r':
                RecoverID()
                   
        changeProfile (password, user, id_user)
        print ("Conta editada\n")

    
    if action == '3':
        id_user = input ("Qual o seu id:\n")

        while id_user.isdigit() == False or  int(id_user) < 0 or int(id_user) > int(len(accountsList) - 1):
                print("Insira um id válido. Caso não se lembre do id, digite 'r' para recuperar o seu id ou 'end' para encerrar o programa")
                id_user = input("Digite seu id:\n")
                if id_user == 'end':
                    quit()
                if id_user == 'r':
                    RecoverID()
                  

        addFriends(id_user)
        print ("Seguindo\n")

    
    if action == '4':
        id_user = input ("Digite seu id:\n")

        while id_user.isdigit() == False or  int(id_user) < 0 or int(id_user) > int(len(accountsList) - 1):
            print("Insira um id válido. Caso não se lembre do id, digite 'r' para recuperar o seu id ou 'end' para encerrar o programa")
            id_user = input("Digite seu id:\n")
            if id_user == 'end':
                quit()
            if id_user == 'r':
                RecoverID()
                   
        postManagement(id_user)
        print ("Receita postada\n")     #cria um txt com a receita

    
    if action == '5':
        id_user = input ("Digite seu id:\n")

        while id_user.isdigit() == False or  int(id_user) < 0 or int(id_user) > int(len(accountsList) - 1):
            print("Insira um id válido. Caso não se lembre do id, digite 'r' para recuperar o seu id ou 'end' para encerrar o programa")
            id_user = input("Digite seu id:\n")
            if id_user == 'end':
                quit()
            if id_user == 'r':
                RecoverID()
                    

        accountRecovery(id_user)
        print ("Conta recuperada\n")


    if action == '6':
        id_user = input("Digite o id do usuário que postou a receita:\n")

        while id_user.isdigit() == False or  int(id_user) < 0 or int(id_user) > int(len(accountsList) - 1):
            print("Insira um id válido. Caso não se lembre do id, digite 'r' para recuperar o seu id ou 'end' para encerrar o programa")
            id_user = input("Digite seu id:\n")
            if id_user == 'end':
                quit()
            if id_user == 'r':
                RecoverID()
                    


        addComment (id_user)


    if action == '7':
        id_user= input ("Qual o seu id?\n")

        while id_user.isdigit() == False or  int(id_user) < 0 or int(id_user) > int(len(accountsList) - 1):
            print("Insira um id válido. Caso não se lembre do id, digite 'r' para recuperar o seu id ou 'end' para encerrar o programa")
            id_user = input("Digite seu id:\n")
            if id_user == 'end':
                quit()
            if id_user == 'r':
                RecoverID()
                    

        show(id_user)
        thisAccountDict = accountsList[int (id_user)]
        user_show = thisAccountDict['user']


    if action == '8':
        id_user = input("Insira o id do usuário que postou a receita:\n")

        while id_user.isdigit() == False or  int(id_user) < 0 or int(id_user) > int(len(accountsList) - 1):
                print("Insira um id válido. Caso não se lembre do id, digite 'end' para encerrar o programa")
                id_user = input("Insira o id do usuário que postou a receita:\n")
                if id_user == 'end':
                    quit()

                
        addAvaliation(id_user)
        
        #print ("Seu post foi:\n")

        #arquivo = open(f"{user_show}.txt", "r")
        #print (arquivo.readlines())
        #print (arquivo.readlines())
        #print (user_show)

    if action == '9':
        break

    
    if action == '10':
        comentarios = []

        id_user = input("Insira o seu ID:\n")

        thisAccountDict = accountsList[int(id_user)]   # Acessa o dicionário do id inserido

        #Verifica se o ID é válido
        while id_user.isdigit() == False or  int(id_user) < 0 or int(id_user) > int(len(accountsList) - 1):
                print("Insira um id válido. Caso não se lembre do id, digite 'end' para encerrar o programa")
                id_user = input("Insira o id do usuário que postou a receita:\n")
                if id_user == 'end':
                    quit()
    
        comentarios = thisAccountDict['comentarios_nas_receitas']     #Passa todos os comentários feitos em receitas para uma lista 

        for i in range(len(lista_de_arquivos_de_receitas_e_topicos)):
            arquivo_receita = lista_de_arquivos_de_receitas_e_topicos[i]   
            for i in range(len(comentarios)):   
                texto_antigo = (f"{thisAccountDict['user'].capitalize()} ({data}): {comentarios[i]}\n")
                remover_comentario_arquivo(arquivo_receita, texto_antigo) 

        comentarios = thisAccountDict['comentarios_nos_topicos']      #Passa todos os comentários feitos em tópicos para uma lista 

        for i in range(len(lista_de_arquivos_de_receitas_e_topicos)):
            arquivo_receita = lista_de_arquivos_de_receitas_e_topicos[i]   
            for i in range(len(comentarios)):   
                texto_antigo = (f"{thisAccountDict['user'].capitalize()} ({data}): {comentarios[i]}\n")  
                remover_comentario_arquivo(arquivo_receita, texto_antigo) 


        for i in range(int(thisAccountDict['id_da_receita'])):
            filename = (f"Receita_{i + 1}_{thisAccountDict['user']}.txt")
            os.remove(filename)

            thisAccountDict['id_da_receita'] = 0

        for i in range(int(thisAccountDict['id_topicos'])):
            filename = (f"Topico_{i + 1}_{thisAccountDict['user']}.txt")
            os.remove(filename)

    
    if action == '11':
        id_user = input("Insira o seu ID\n")

        while id_user.isdigit() == False or  int(id_user) < 0 or int(id_user) > int(len(accountsList) - 1):
                print("Insira um id válido. Caso não se lembre do id, digite 'end' para encerrar o programa")
                id_user = input("Insira o id do usuário que postou a receita:\n")
                if id_user == 'end':
                    quit()
        
        topicos(id_user)

    if action == '12':
        id_user = input("Insira o ID do usuário que publicou o tópico\n")

        while id_user.isdigit() == False or  int(id_user) < 0 or int(id_user) > int(len(accountsList) - 1):
                print("Insira um id válido. Caso não se lembre do id, digite 'end' para encerrar o programa")
                id_user = input("Insira o id do usuário que postou a receita:\n")
                if id_user == 'end':
                    quit()

        adicionar_comentario_topico(id_user)

    if action == '13':
        id_user = input("Insira o seu ID:\n")

        while id_user.isdigit() == False or  int(id_user) < 0 or int(id_user) > int(len(accountsList) - 1):
                print("Insira um id válido. Caso não se lembre do id, digite 'end' para encerrar o programa")
                id_user = input("Insira o id do usuário que postou a receita:\n")
                if id_user == 'end':
                    quit()

        privacidade(id_user)
    
    if action == '14':
        id_user = input("Insira o seu ID:\n")


        while id_user.isdigit() == False or  int(id_user) < 0 or int(id_user) > int(len(accountsList) - 1):
                print("Insira um id válido. Caso não se lembre do id, digite 'end' para encerrar o programa")
                id_user = input("Insira o id do usuário que postou a receita:\n")
                if id_user == 'end':
                    quit()

        privacidade_desativar(id_user)


    if action == '15':
        RecoverID()

   
