import os
from account import *
from avaliacoes import *

class Sistema():
    def __init__(self):
        self.accountsDict = {}
        self.receitasDict = {}
        self.AccountNumber = 0
        self.numeroDeContas = self.AccountNumber

    def logarNaConta(self):
        conta = Sistema.contaUsuario(self)

        print(f"\nVocê fez login na conta número {conta.accountNumber}.")


        while True:
            
            print ("\nDigite 1 para acessar opções relacionadas à sua conta.")
            print ("Digite 2 para acessar opções relacionadas à receitas.")
            print ("Digite 3 para acessar opções relacionadas a tópicos.")
            print ("Digite 4 para ver o perfil de outro usuário.")
            print ("Digite 5 para acessar a aba de notificações.")
            print ("Digite 6 para criar outra conta ou fazer login em outra conta.")
            print ("Digite 20 para encerrar o programa.")

            action = input("\nInsira a opção: ")

            if action == '1':
                while True:
                    
                    print("\n--------CONFIGURAÇÃO DA CONTA--------")

                    print ("\nDigite 1 para editar a sua conta.")
                    print ("Digite 2 para mostrar o seu nome de usuário e o número da sua conta.")
                    print ("Digite 3 para ver o seu perfil.")
                    print ("Digite 4 para ativar o modo de privacidade. Apenas pessoas que você segue podem avaliar e comentar em suas receitas e tópicos e ver o seu perfil.")
                    print ("Digite 5 para desativar o modo de privacidade. Todos poderão comentar em suas receitas e tópicos.")
                    print ("Digite 6 para adicionar amigos.")
                    print ("Digite 7 para remover um amigo.")
                    print ("Digite 8 para mostrar os seus amigos.")
                    print ("Digite 9 para bloquear um usuário específico.")
                    print ("Digite 10 para desbloquear um usuário específico.")
                    print ("Digite 11 para mostrar os usuários bloqueados.")
                    print ("Digite 12 para escrever uma mensagem para outro usuário.")
                    print ("Digite 13 para mostrar o chat com um usuário.")
                    print ("Digite 14 para seguir um usuário.")
                    print ("Digite 15 para parar de seguir.")
                    print ("Digite 16 para ver quem você está seguindo.")
                    print ("Digite 20 para retornar ao menu.")

                    action1 = input("\nInsira a opção: ")

                    if action1 == '1':
                        EditarConta.editar(self, conta)

                    if action1 == '2':
                        print(f"Nome de usuário: {conta.username}")
                        print(f"O número da sua conta é {conta.accountNumber}.\n")

                    if action1 == '3':
                        conta.show()

                    if action1 == '4':
                        conta.AtivarPrivacidade()

                    if action1 == '5':
                        conta.DesativarPrivacidade()

                    if action1 == '6':
                        login.addFriends(conta)

                    if action1 == '7':
                        login.removeFriends(conta)
                    
                    if action1 == '8':
                        conta.showFriends()

                    if action1 == '9':
                        login.bloquearUsuario(conta)
                    
                    if action1 == '10':
                        login.desbloquearUsuario(conta)
                    
                    if action1 == '11':
                        conta.showBloqueados()
                    
                    if action1 == '12':
                        Mensagem.escreverMensagem(self, conta)

                    if action1 == '13':
                        Mensagem.mostrarChat(self, conta)

                    if action1 == '14':
                        Inscricoes.seguir(self, conta)
                    
                    if action1 == '15':
                        Inscricoes.pararDeSeguir(self, conta)
                    
                    if action1 == '16':
                        conta.mostrarQuemEstaSeguindo()
                

                    if action1 == '20':
                        break

            if action == '2':
                while True:

                    print ("\n------RECEITAS------")

                    print ("\nDigite 1 para postar uma receita.")
                    print ("Digite 2 para avaliar uma receita.")
                    print ("Digite 3 para comentar em uma receita.")
                    print ("Digite 4 para apagar um comentário de um usuário em uma receita sua.")
                    print ("Digite 5 para apagar os seus comentários nas receitas.")
                    print ("Digite 6 para apagar todas as suas receitas.")
                    print ("Digite 7 para procurar uma receita com a palavra/frase inserida.")
                    print ("Digite 8 para visualizar alguma receita.")
                    print ("Digite 20 para retornar ao menu.")

                    action3 = input("\nInsira a opção: ")

                    if action3 == '1':
                        Receitas.criarReceita(self, conta)
            
                    if action3 == '2':
                        Receitas.avaliarReceitas(self, conta)
            
                    if action3 == '3':
                        Receitas.postComment(self, conta)

                    if action3 == '4':
                        GerenciarReceitasETopicos.usernameComentario(self, conta, 0)

                    if action3 == '5':
                        GerenciarReceitasETopicos.deletarComentarioReceita(self, conta)

                    if action3 == '6':
                        GerenciarReceitasETopicos.ApagarArquivoReceita(self, conta)
                    
                    if action3 == '7':
                        Sistema.filtroDeReceitas(self)
                    
                    if action3 == '8':
                        GerenciarReceitasETopicos.visualizarReceita(self, conta)
                    
                    if action3 == '20':
                        break


            if action == '3':
                while True:
                    print ("\n------TÓPICOS------\n")

                    print ("\nDigite 1 para postar um tópico de discussão.")
                    print ("Digite 2 para comentar em um tópico de discussão.")
                    print ("Digite 3 para apagar um comentário de um usuário em um tópico seu.")
                    print ("Digite 4 para apagar os seus comentários nos tópicos.")
                    print ("Digite 5 para apagar todos os seus tópicos.")
                    print ("Digite 6 para filtrar os tópicos por tema.")
                    print ("Digite 7 para visualizar algum tópico.")
                    print ("Digite 20 para retornar ao menu.")

                    action4 = input("\nInsira a opção: ")

                    if action4 == '1':
                        Topicos.criarTopico(self, conta)

                    if action4 == '2':
                        Topicos.postComment(self, conta)

                    if action4 == '3':
                        GerenciarReceitasETopicos.usernameComentario(self, conta, 1)

                    if action4 == '4':
                        GerenciarReceitasETopicos.deletarComentarioTopico(self, conta)

                    if action4 == '5':
                        GerenciarReceitasETopicos.ApagarArquivoTopico(self, conta)
                    
                    if action4 == '6':
                        Sistema.filtroDeTopicos(self)
                    
                    if action4 == '7':
                        GerenciarReceitasETopicos.visualizarTopico(self, conta)
                    
                    if action4 == '20':
                        break
            
            if action == '4':
                login.showUserProfile(conta)


            if action == '5':
                while True:

                    print("\n------NOTIFICAÇÕES------\n")

                    if len(conta.listaDeMensagensNaoLidas) > 0:
                        if len(conta.listaDeMensagensNaoLidas) == 1:
                            print(f"\nVocê tem {len(conta.listaDeMensagensNaoLidas)} mensagem não lida.")
                        else:
                            print(f"\nVocê tem {len(conta.listaDeMensagensNaoLidas)} mensagens não lidas.")
            
                    print("\nDigite 1 para ver todas as mensagens recebidas.")
                    print("Digite 2 para ver as mensagens não lidas.")
                    print("Digite 3 para apagar as mensagens recebidas.")
                    print("Digite 4 para ver se tem avaliações novas em alguma receita sua.")
                    print("Digite 5 para ver se alguém que você segue postou uma receita nova.")
                    print("Digite 20 para retornar ao menu.")

                    action2 = input("\nInsira a opção: ")
                    
                    if action2 == '1':
                        conta.verMensagens()
                    
                    if action2 == '2':
                        conta.verMensagensNaoLidas()
                
                    if action2 == '3':
                        conta.deletarMensagens()

                    if action2 == '4':
                        existeReceitaAvaliada = False
                        if len(conta.listaDeReceitas) > 0:
                            print("\n")
                            for i in range(len(conta.listaDeReceitas)):
                                id = f"{conta.accountNumber}{i + 1}"
                                if id in conta.dictAvaliacoesRecebidas and conta.dictAvaliacoesRecebidas[id] != 0:
                                    print(f"{conta.dictAvaliacoesRecebidas[id]}\n")
                                    conta.dictAvaliacoesRecebidas[id] = 0
                                    existeReceitaAvaliada = True
                                    Receitas.atualizarAvaliacoesNovas(self, id)
                        if existeReceitaAvaliada == False:
                            print("\nSem avaliações novas.")
                    
                    if action2 == '5':
                        conta.inscricoes()

                    if action2 == '20':
                        break
            
            if action == '6':
                return

            if action == '20':
                print("\nPrograma encerrado.\n")
                return False
            
    def filtroDeReceitas(self):
        palavraAceitavel = False
        listaDasReceitasAchadas = []
        quantidadeDeReceitasEncontradas = 0

        while palavraAceitavel == False:
            palavra = input("Escreva a frase/palavra que você quer procurar nas receitas. A frase/palavra precisa ter pelo menos 3 letras: ")
            if len(palavra.strip()) >= 3:
                palavraAceitavel = True

        for i in range(self.numeroDeContas):
            conta = self.accountsDict[i]
            for j in range(len(conta.listaDeReceitas)):
                filename = conta.listaDeReceitas[j]
                conteudoEscritoNaReceita = conta.conteudoEscritoNaReceita[j]
                achou = GerenciarReceitasETopicos.filtroDeReceitas(self, filename, palavra, conteudoEscritoNaReceita) 
                if achou == True:
                    quantidadeDeReceitasEncontradas += 1
                    frase = f"Receita {j + 1} do usuário {conta.username} (ID: {conta.accountNumber})"
                    listaDasReceitasAchadas.append(frase)
                    
        if quantidadeDeReceitasEncontradas == 0:
            print("\nNenhuma receita foi encontrada.")
        elif quantidadeDeReceitasEncontradas == 1:
            print(f"\n{quantidadeDeReceitasEncontradas} receita foi encontrada.\n")
        else:
            print(f"\n{quantidadeDeReceitasEncontradas} receitas foram encontradas.\n")

        for receitas in listaDasReceitasAchadas:
            print(receitas)
    
    def filtroDeTopicos(self):
        palavraAceitavel = False
        listaDosTopicosAchados = []
        quantidadeDeTopicosEncontrados = 0


        while palavraAceitavel == False:
            palavra = input("Escreva o tema que você quer encontrar nos tópicos. A palavra precisa ter pelo menos 3 letras: ")
            if len(palavra.strip()) >= 3:
                palavraAceitavel = True


        for i in range(self.numeroDeContas):
            conta = self.accountsDict[i]
            for j in range(len(conta.listaDeTopicos)):
                filename = conta.listaDeTopicos[j]
                conteudoEscritoNoTopico = conta.conteudoEscritoNoTopico[j]
                achou = GerenciarReceitasETopicos.filtroDeReceitas(self, filename, palavra, conteudoEscritoNoTopico) 
                if achou == True:
                    quantidadeDeTopicosEncontrados += 1
                    frase = f"Tópico {j + 1} do usuário {conta.username} (ID: {conta.accountNumber})"
                    listaDosTopicosAchados.append(frase)

        if quantidadeDeTopicosEncontrados == 0:
            print("\nNenhuma tópico foi encontrado.")
        elif quantidadeDeTopicosEncontrados == 1:
            print(f"\n{quantidadeDeTopicosEncontrados} tópico foi encontrado.\n")
        else:
            print(f"\n{quantidadeDeTopicosEncontrados} tópicos foram encontrados.\n")

        for topicos in listaDosTopicosAchados:
            print(topicos)


    
    def apagarAvaliacoes(self, conta):
        idReceita = conta.idReceita
        for i in range(self.numeroDeContas):  #Algoritmo lento, mas foi o melhor que eu pensei.
            for j in range(idReceita):
                id = f"{conta.accountNumber}{j + 1}"
                conta1 = self.accountsDict[i]
                if id in conta1.listaDeReceitasAvaliadas:
                    conta1.listaDeReceitasAvaliadas.remove(id)

    def notificacaoAosInscritosReceita(self, conta):
        idReceita = conta.idReceita
        for i in range(len(conta.listaDeSeguidores)):
            conta1 = self.accountsDict[conta.listaDeSeguidores[i]]
            aviso = f"{conta.username} publicou uma nova receita (Receita {idReceita})."
            conta1.listaDeNotificacoesDeInscricoes.append(aviso)
    
    def notificacaoAosInscritosTopicos(self, conta):
        idTopico = conta.idTopico
        for i in range(len(conta.listaDeSeguidores)):
            conta1 = self.accountsDict[conta.listaDeSeguidores[i]]
            aviso = f"{conta.username} publicou um novo tópico (Tópico {idTopico})."
            conta1.listaDeNotificacoesDeInscricoes.append(aviso)
        
            
    def criarConta(self, name, password, username):
        conta = Account(name, password, username, self.AccountNumber)
        newAccountNumber = self.AccountNumber
        self.accountsDict[newAccountNumber] = conta

        self.AccountNumber = self.AccountNumber + 1
        self.numeroDeContas = self.AccountNumber
        return newAccountNumber
    
    def abrirConta(self):
        print("   Abrindo Conta  ")
        nome = input("Insira o seu nome: ")
        password = input("Insira a sua senha: ")  
        while True:
            username = input("Insira um nome de usuário: ")
            if Sistema.validarUsernameContaCriada(self, username):
                print("Esse nome de usuário já está sendo utilizado. Insira outro.")
            else:
                break


        userAccountNumber = self.criarConta(nome, password, username)
        print("O número da sua conta é: ", userAccountNumber)
        print("")


    def recoverID(self):
        username = input("Insira o seu nome de usuário: ")
        conta = Sistema.validarUsername(self, username)

        password = input("Insira a senha: ")
        conta.ChecarSenha(password)

        print(f"\nO número da sua conta é {conta.accountNumber}.")

    def accountRecovery(self):
        accountNumber = self.verificarNumeroDaConta(1)
        conta = self.accountsDict[accountNumber]
        self.verificarSenha(conta)
        print(f"Nome de usuário: {conta.username}\n")
   

    def showUserProfile(self, conta):
        amigo = False
        accountNumber = Sistema.verificarNumeroDaConta(self, 7)
        contaOutroUsuario = self.accountsDict[accountNumber]

        if conta.username in contaOutroUsuario.listaDeAmigos:
            amigo = True

        if contaOutroUsuario.modoPrivacidade == 1 and amigo == False:
            print("\nVocê não pode ver o perfil desse usuário porque ele está com o modo de privacidade ativado.")
        else:
            contaOutroUsuario.showOutroUser()


    def bloquearUsuario(self, conta):
        numeroDaConta = Sistema.verificarNumeroDaConta(self, 4)
        contaParaBloquear = Sistema.username(self, numeroDaConta)

        if contaParaBloquear.accountNumber == conta.accountNumber:
            print("\nVocê não pode se bloquear.")
            return


        if contaParaBloquear.username in conta.usuariosBloqueados:
            print("\nEsse usuário já foi bloqueado.")
            return
        
        if contaParaBloquear.username in conta.listaDeAmigos:
            print("\nEsse usuário foi bloqueado e removido da lista de amigos")
            conta.usuariosBloqueados.append(contaParaBloquear.username)
            conta.listaDeAmigos.remove(contaParaBloquear.username)
            return
        
        conta.usuariosBloqueados.append(contaParaBloquear.username)
        print ("\nUsuário bloqueado.")

    def desbloquearUsuario(self, conta):
        numeroDaConta = Sistema.verificarNumeroDaConta(self, 5)

        contaParaDesbloquear = Sistema.username(self, numeroDaConta)

        if contaParaDesbloquear.accountNumber == conta.accountNumber:
            print("\nVocê não pode se bloquear.")
            return

        if contaParaDesbloquear.username not in conta.usuariosBloqueados:
            print("\nEsse usuário não está bloqueado.")
            return
        
        conta.usuariosBloqueados.remove(contaParaDesbloquear.username)

        print ("\nUsuário desbloqueado.")

    def validarUsername(self, username):
        while True:
            for i in range(len(self.accountsDict)):
                conta = self.accountsDict[i]
                if username == conta.username:
                    return conta
            username = input("Não achamos esse nome de usuário. Insira novamente: ")

    def validarUsernameContaCriada(self, username):
        for conta in self.accountsDict.values():
            if username == conta.username:
                return True
        return False

    
    def showProfile(self):
        conta = Sistema.contaUsuario(self)
        conta.show()

    def verificarNumeroDaConta(self, opcao):
        accountNumberAceitavel = False
        if opcao == 1:
            accountNumber = input("Insira o ID da sua conta: ")
        elif opcao == 2:
            accountNumber = input("Insira o ID de quem você quer adicionar: ")
        elif opcao == 3:
            accountNumber = input("Insira o ID de quem você quer remover: ")
        elif opcao == 4:
            accountNumber = input("Insira o ID de quem você quer bloquear: ")
        elif opcao == 5:
            accountNumber = input("Insira o ID de quem você quer desbloquear: ")
        elif opcao == 6:
            accountNumber = input("Insira o ID da conta do usuário: ")
        elif opcao == 7:
            accountNumber = input("Insira o ID do usuário que você quer ver: ")


        while accountNumberAceitavel == False:
                if  accountNumber.isdigit() == False or int(accountNumber) >= self.numeroDeContas or int(accountNumber) < 0:
                    accountNumber = input("ID incorreto. Insira novamente.")
                else:
                    accountNumberAceitavel = True

        if accountNumberAceitavel == True:
            return int(accountNumber)
    
    def contaUsuario(self):
        accountNumber = self.verificarNumeroDaConta(1)
        conta = self.accountsDict[accountNumber]
        self.verificarSenha(conta)
        return conta
    
    def contaAmigo(self, adicionar):
        if adicionar == 1:
            accountNumber = self.verificarNumeroDaConta(2)
        else:
            accountNumber = self.verificarNumeroDaConta(3)

        conta_amigo = self.accountsDict[accountNumber]
        return conta_amigo
    
    def verificarSenha(self, conta):
        password = input("Insira a sua senha: ")
        conta.ChecarSenha(password)

    def addFriends(self, conta):
        userAmigo = Sistema.contaAmigo(self, 1)

        if userAmigo.accountNumber == conta.accountNumber:
            print ("\nVocê não pode se adicionar.")
            return

        if userAmigo.username in conta.listaDeAmigos:
            print("\nEsse usuário já é seu amigo.")
            return

        if userAmigo.username in conta.usuariosBloqueados:
            print("\nEsse usuário foi desbloqueado e adicionado na sua lista de amigos.")
            conta.usuariosBloqueados.remove(userAmigo.username)
            conta.listaDeAmigos.append(userAmigo.username)
            return

        conta.listaDeAmigos.append(userAmigo.username)

        print("\nAmigo adicionado.")


    def removeFriends(self, conta):
        userAmigo = Sistema.contaAmigo(self,0)

        if userAmigo.username not in conta.listaDeAmigos:
            print("\nEsse usuário não é seu amigo.")
            return
        conta.listaDeAmigos.remove(userAmigo.username)

        print("\nUsuário removido da lista de amigos.")
   

    def username(self, accountNumber):
        conta = self.accountsDict[accountNumber]
        return conta
            
class EditarConta():
    def __init__(self):
        self

    def editar(self, conta):
        oldUsername = conta.username
        while True:
            username = input("Insira o seu novo nome de usuário: ")
            if Sistema.validarUsernameContaCriada(self, username):
                print("Esse nome de usuário já está sendo utilizado. Insira outro.")
            else:
                break
        
        conta.username = username

        conta.password = input("Insira a sua nova senha:")

        for i in range(len(conta.arquivosComentariosReceitas)):
            if len(conta.arquivosComentariosReceitas) != 0:
                filename = conta.arquivosComentariosReceitas[i]
            if len(conta.listaDeComentariosReceitas) != 0:
                comentario = conta.listaDeComentariosReceitas[i]

            if os.path.isfile(filename):
                with open(filename, 'r', encoding = 'utf8') as file:
                    conteudo = file.read()

                conteudoModificado = conteudo.replace(f"{oldUsername.capitalize()} (ID: {conta.accountNumber}): {comentario}\n", f"{conta.username.capitalize()} (ID: {conta.accountNumber}): {comentario}\n")

                with open(filename, 'w', encoding = "utf8") as file:
                    file.writelines(conteudoModificado)



        for i in range(len(conta.listaDeReceitas)):
            filename = conta.listaDeReceitas[i]

            if os.path.isfile(filename):
                with open(filename, 'r', encoding = 'utf8') as file:
                    conteudo = file.read()

                conteudoModificado = conteudo.replace(f"Esta receita foi postada pelo usuário {oldUsername.capitalize()}", f"Esta receita foi postada pelo usuário {conta.username.capitalize()}")

                with open(filename, 'w', encoding = "utf8") as file:
                    file.writelines(conteudoModificado)



        for i in range(len(conta.listaDeTopicos)):
            filename = conta.listaDeTopicos[i]
            with open(filename, 'r', encoding = 'utf8') as file:
                conteudo = file.read()

            conteudoModificado = conteudo.replace(f"Este tópico foi postado pelo usuário {oldUsername.capitalize()}", f"Este tópico foi postado pelo usuário {conta.username.capitalize()}")

            with open(filename, 'w', encoding = "utf8") as file:
                file.writelines(conteudoModificado)

        for i in range(len(conta.arquivosComentariosTopicos)):
            if len(conta.arquivosComentariosTopicos) != 0:
                filename = conta.arquivosComentariosTopicos[i]
            if len(conta.listaDeComentariosTopicos) != 0:
                comentario = conta.listaDeComentariosTopicos[i]

            if os.path.isfile(filename):
                with open(filename, 'r', encoding = 'utf8') as file:
                    conteudo = file.read()

                conteudoModificado = conteudo.replace(f"{oldUsername.capitalize()} (ID: {conta.accountNumber}): {comentario}\n", f"{conta.username.capitalize()} (ID: {conta.accountNumber}): {comentario}\n")

                with open(filename, 'w', encoding = "utf8") as file:
                    file.writelines(conteudoModificado)

        for i in range(len(conta.arquivosDeChat)):
            if len(conta.arquivosDeChat) != 0:
                filename = conta.arquivosDeChat[i]
            if len(conta.mensagensFeitas) != 0:
                comentario = conta.mensagensFeitas[i]

            if os.path.isfile(filename):
                with open(filename, 'r', encoding = 'utf8') as file:
                    conteudo = file.read()

                conteudoModificado = conteudo.replace(f"{oldUsername}: {comentario}\n", f"{conta.username}: {comentario}\n")

                with open(filename, 'w', encoding = "utf8") as file:
                    file.writelines(conteudoModificado)
      
class Mensagem():
    def __init__(self):
        self.comentarios = []

    def escreverMensagem(self, conta1):
        accountNumber = Sistema.verificarNumeroDaConta(self, 6)
        conta = Sistema.username(self, accountNumber)

        mensagemAceitavel = False

        filename = f"Chat{conta.accountNumber}+{conta1.accountNumber}"
        filename2 = f"Chat{conta1.accountNumber}+{conta.accountNumber}"


        if filename2 in conta1.arquivosDeChat:
            Mensagem.chat(self, conta1, conta, filename2)
        elif filename not in conta1.arquivosDeChat:

            if conta.username in conta1.usuariosBloqueados:
                print("\nVocê não pode mandar uma mensagem para esse usuário.")
                return

            if conta.modoPrivacidade == 1 and conta.username not in conta1.listaDeAmigos:
                print("\nVocê não pode mandar uma mensagem para esse usuário.")
                return

            if conta.accountNumber == conta1.accountNumber:
                print("\nVocê não pode enviar uma mensagem para você mesmo.")
                return
            
            while mensagemAceitavel == False:
                mensagem = input("Escreva uma mensagem: ")
                if mensagem != "":
                    mensagemAceitavel = True
                else:
                    mensagemAceitavel = False

            mensagem2 = f"{conta1.username}: {mensagem}."

            print(mensagem2)

            conta.mensagensFeitas.append(mensagem)
            conta.listaDeMensagens.append(mensagem2)
            conta.listaDeMensagensNaoLidas.append(mensagem2)
            conta1.arquivosDeChat.append(filename)
            conta.arquivosDeChat.append(filename)

            with open(filename, "w", encoding = "utf8") as file:
                if True:
                    file.write(f"{conta1.username}: {mensagem}\n")
        else:
            Mensagem.chat(self, conta1, conta, filename)

        
        
    def chat(self, conta1, conta, filename): 
        mensagemAceitavel = False

        with open(filename, "a", encoding = "utf8") as file:
            if True:
                while mensagemAceitavel == False:
                    mensagem = input("Escreva uma mensagem: ")
                    if mensagem != "":
                        mensagemAceitavel = True
                    else:
                        mensagemAceitavel = False
                mensagem2 = f"{conta.username}: {mensagem}"
                conta.listaDeMensagens.append(mensagem2)
                conta.listaDeMensagensNaoLidas.append(mensagem2)
                file.write(f"{conta1.username}: {mensagem}\n")


    def mostrarChat(self, conta1):
        accountNumber = Sistema.verificarNumeroDaConta(self, 6)
        conta = Sistema.username(self, accountNumber)

        filename = f"Chat{conta.accountNumber}+{conta1.accountNumber}"
        filename2 = f"Chat{conta1.accountNumber}+{conta.accountNumber}"

        if os.path.isfile(filename):
            with open(filename, "r", encoding = "utf-8") as file:
                conteudo = file.read()
                print(f"\nSua conversa com {conta.username}\n")
                print(conteudo)
        elif os.path.isfile(filename2):
            with open(filename2, "r", encoding = "utf-8") as file:
                conteudo = file.read()
                print(f"\nSua conversa com {conta.username}:\n")
                print(conteudo)
        else:
            print("\nVocê não tem uma conversa com esse usuário.")

class Inscricoes():
    def __init__(self):
        self
    
    def seguir(self, conta):
        accountNumber = Sistema.verificarNumeroDaConta(self, 6)
        conta1 = Sistema.username(self, accountNumber)

        if conta.accountNumber == conta1.accountNumber:
            print("\nVocê não pode se seguir.")
            return

        if conta1.username in conta.listaDeQuemEstaSeguindo:
            print("\nVocê já segue esse usuário.")
            return

        conta.listaDeQuemEstaSeguindo.append(conta1.username)
        conta1.listaDeSeguidoresUsername.append(conta.username)
        conta1.listaDeSeguidores.append(conta.accountNumber)
    
    def pararDeSeguir(self, conta):
        accountNumber = Sistema.verificarNumeroDaConta(self, 6)
        conta1 = Sistema.username(self, accountNumber)

        if conta.accountNumber == conta1.accountNumber:
            print("\nVocê não pode se seguir.")
            return
        
        if conta1.username not in conta.listaDeQuemEstaSeguindo:
            print("\nVocê não segue esse usuário.")
            return
        
        conta.listaDeQuemEstaSeguindo.remove(conta1.username)
        conta1.listaDeSeguidoresUsername.remove(conta.username)
        conta1.listaDeSeguidores.remove(conta.accountNumber)

class Receitas():
    def __init__(self):
        self.receitasDict = {}

    def contaDeQuemPostouAReceita(self):
        accountNumberAceitavel = False
        
        accountNumber = input("Insira o ID de quem postou a receita: ")

        while accountNumberAceitavel == False:
                if  accountNumber.isdigit() == False or int(accountNumber) >= self.numeroDeContas or int(accountNumber) < 0:
                    accountNumber = input("ID incorreto. Insira novamente: ")
                else:
                    accountNumberAceitavel = True

        conta = Sistema.username(self, int(accountNumber))
        
        return conta

        
    def idDaReceita(self, conta):
        idAceitavel = False
        idReceita = input("Insira o ID da receita: ")
        while idAceitavel == False:
            if idReceita.isdigit() == False or int(idReceita) > len(conta.listaDeReceitas) or int(idReceita) < 1:
                idReceita = input("Esse usuário não tem receitas com esse ID, insira novamente: ")
            else:
                idAceitavel = True

        return idReceita
       
    def criarReceita(self, conta):
        filename = f"Receita_{conta.idReceita}_userID({conta.accountNumber}).txt" 


        with open(filename, "w", encoding = "utf8") as file:
            if True:
                file.write(f"Esta receita foi postada pelo usuário {conta.username.capitalize()}\n\n")
                file.write(f"Avaliação média da receita: 0.0  (0 avaliações).\n\n")
                nomeDaReceita = input("Escreva o nome da receita: ")
                file.write(f"Nome da receita: {nomeDaReceita}\n\n")
                ingredientes = input("Escreva os ingredientes: ")
                file.write(f"Ingredientes: {ingredientes}\n\n")
                modoDePreparo = input("Escreva o modo de preparo: ")
                file.write(f"Modo de preparo: {modoDePreparo}\n\n\n")
                file.write("Comentários:\n\n")

        conteudo = f"{nomeDaReceita}{ingredientes}{modoDePreparo}"
        
        conta.conteudoEscritoNaReceita.append(conteudo)
        
        Sistema.notificacaoAosInscritosReceita(self, conta)
        
        conta.listaReceitas(filename)

    

    def avaliarReceitas(self, contaAvaliador):
        amigo = True
        conta = Receitas.contaDeQuemPostouAReceita(self)

        if conta.accountNumber == contaAvaliador.accountNumber:
            print("\nVocê não pode avaliar a sua própria receita.\n")
            return

        if conta == False:
            return

        if conta.idReceita == 1:
            print("\nEsse usuário não tem receitas postadas.\n")
            return
        
        

        if len(conta.usuariosBloqueados) > 0:
            for i in range(len(conta.usuariosBloqueados)):
                if contaAvaliador.username == conta.usuariosBloqueados[i]:
                    print("\nVocê não pode avaliar as receitas desse usuário. Você está bloqueado.")
                    return
        
        if int(conta.modoPrivacidade) == 1:
            for i in range(len(conta.listaDeAmigos)):
                if contaAvaliador.username != conta.listaDeAmigos[i]:
                    amigo = False
                else:
                    amigo = True
            
        if len(conta.listaDeAmigos) == 0 and int(conta.modoPrivacidade) == 1:
            amigo = False


        if amigo == False:
            print("\nO usuário que postou a receita está com o modo de privacidade ativo. Apenas amigos podem avaliar.\n")
            return

        idReceita = Receitas.idDaReceita(self, conta)

        filename = f"Receita_{idReceita}_userID({conta.accountNumber}).txt"

        id = f"{conta.accountNumber}{idReceita}"

        if len(contaAvaliador.listaDeReceitasAvaliadas) > 0:
            for i in range(len(contaAvaliador.listaDeReceitasAvaliadas)):
                if id == contaAvaliador.listaDeReceitasAvaliadas[i]:
                    print("\nVocê já avaliou essa receita. Insira outra opção.\n")
                    return
            

        receita = self.receitasDict.get(id)
        if receita is None:
            receita = AvaliacaoDeReceitas()
            self.receitasDict[id] = receita

        avaliacao_aceitavel = False
        while avaliacao_aceitavel == False:
            avaliacao = input("Avalie a receita com uma nota de 0 a 5: ")
            if avaliacao.isdigit() and 0 <= int(avaliacao) <= 5:
                avaliacao_aceitavel = True
            else:
                print("Só é possível inserir uma nota de 0 a 5.\n")

        receita.atualizarAvaliacao(avaliacao)

        self.receitasDict[id] = receita


        if receita.quantidadeDeAvaliacoes == 2:
            textoAntigo = f"Avaliação média da receita: {receita.notaAntiga:.1f}  ({receita.quantidadeDeAvaliacoesAntigas} avaliação)"
        else:
            textoAntigo = f"Avaliação média da receita: {receita.notaAntiga:.1f}  ({receita.quantidadeDeAvaliacoesAntigas} avaliações)"
        if receita.quantidadeDeAvaliacoes == 1:
            textoNovo = f"Avaliação média da receita: {receita.notaMedia:.1f}  ({receita.quantidadeDeAvaliacoes} avaliação)"
        else:
            textoNovo = f"Avaliação média da receita: {receita.notaMedia:.1f}  ({receita.quantidadeDeAvaliacoes} avaliações)"

        contaAvaliador.listaDeReceitasAvaliadas.append(id)

        with open(filename, 'r', encoding="utf8") as file:
            conteudo = file.read()

        conteudo_modificado = conteudo.replace(textoAntigo, textoNovo)

        with open(filename, 'w', encoding="utf8") as file:
            file.writelines(conteudo_modificado)

        if self.receitasDict[id].avaliacoesNovas == 1:  
            avaliacoes = f"{self.receitasDict[id].avaliacoesNovas} usuário avaliou a sua receita {idReceita}"
        elif self.receitasDict[id].avaliacoesNovas > 1:
            avaliacoes = f"{self.receitasDict[id].avaliacoesNovas} usuários avaliaram a sua receita {idReceita}"
        
        conta.dictAvaliacoesRecebidas[id] = avaliacoes

      
        print("\nReceita Avaliada.\n")

    def atualizarAvaliacoesReceitaDeletada(self, id):
        self.receitasDict[id] = None

    def atualizarAvaliacoesNovas(self, id):
        self.receitasDict[id].avaliacoesNovas = 0

    def postComment(self, conta1):
        amigo = True

        conta = Receitas.contaDeQuemPostouAReceita(self)
       
        if conta == False:
            return
        
        if conta.idReceita == 1 and conta1.accountNumber == conta.accountNumber:
            print("\nVocê não tem receitas postadas.")
            return

        if conta.idReceita == 1:
            print("\nEsse usuário não tem receitas postadas.")
            return

        if len(conta.usuariosBloqueados) > 0:
            for i in range(len(conta.usuariosBloqueados)):
                if conta1.username == conta.usuariosBloqueados[i]:
                    print("\nVocê não pode comentar nas receitas desse usuário. Você está bloqueado.")
                    return

        if int(conta.modoPrivacidade) == 1:
            for i in range(len(conta.listaDeAmigos)):
                if conta1.username != conta.listaDeAmigos[i]:
                    amigo = False
                else:
                    amigo = True
            
        if len(conta.listaDeAmigos) == 0 and int(conta.modoPrivacidade) == 1:
            amigo = False


        if amigo == False:
            print("\nO usuário que postou a receita está com o modo de privacidade ativo. Apenas amigos podem comentar.\n")
        else:
            idReceita = Receitas.idDaReceita(self, conta)
            filename = f"Receita_{idReceita}_userID({conta.accountNumber}).txt"

        
            with open(filename, "a", encoding = "utf8") as file:
                if True:
                    comentario = input("Insira um comentário: ")
                    file.write(f"{conta1.username.capitalize()} (ID: {conta1.accountNumber}): {comentario}\n")

            conta1.listaDeComentariosReceitas.append(comentario)
            conta1.arquivosComentariosReceitas.append(filename)

            print("\nComentário postado.")           

class Topicos():
    def __init__(self):
        self.topicosDict = {}

    def contaDeQuemPostouOTopico(self):
        accountNumberAceitavel = False
        
        accountNumber = input("Insira o ID de quem postou o tópico: ")

        while accountNumberAceitavel == False:
                if  accountNumber.isdigit() == False or int(accountNumber) >= self.numeroDeContas or int(accountNumber) < 0:
                    accountNumber = input("ID incorreto. Insira novamente: ")
                else:
                    accountNumberAceitavel = True

        conta = Sistema.username(self, int(accountNumber))
        
        return conta

        
    def idDoTopico(self, conta):
        idAceitavel = False
        idTopico = input("Insira o ID do tópico: ")

        while idAceitavel == False:
            if idTopico.isdigit() == False or int(idTopico) > len(conta.listaDeTopicos) or int(idTopico) < 1:
                idTopico = input("Esse usuário não tem tópicos com esse ID, insira novamente: ")
            else:
                idAceitavel = True

        return idTopico
       
    def criarTopico(self, conta):
        filename = f"Topico_{conta.idTopico}_userID({conta.accountNumber}).txt"
        with open(filename, "w", encoding = "utf8") as file:
            if True:
                file.write(f"Este tópico foi postado pelo usuário {conta.username.capitalize()}\n\n")
                temaDoTopico = input("Escreva o tema do tópico: ")
                file.write(f"Tema do tópico: {temaDoTopico}\n\n")
                file.write("Comentarios:\n\n")

        conteudo = f"{temaDoTopico}"

        conta.conteudoEscritoNoTopico.append(conteudo)

        Sistema.notificacaoAosInscritosTopicos(self, conta)


        conta.listaTopicos(filename)

    def postComment(self, conta1):
        amigo  = True
        conta = Topicos.contaDeQuemPostouOTopico(self)

        if conta == False:
            return
        
        if conta.idTopico == 1 and conta1.accountNumber == conta.accountNumber:
            print("\nVocê não tem tópicos postados.")
            return

        if conta.idTopico == 1:
            print("\nEsse usuário não tem tópicos postados.")
            return

        if len(conta.usuariosBloqueados) > 0:
            if conta1.username in conta.usuariosBloqueados:
                print("\nVocê não pode comentar nos tópicos desse usuário. Você está bloqueado.")
                return

        
        if int(conta.modoPrivacidade) == 1:
            for i in range(len(conta.listaDeAmigos)):
                if conta1.username != conta.listaDeAmigos[i]:
                    amigo = False
                else:
                    amigo = True
            
        if len(conta.listaDeAmigos) == 0 and int(conta.modoPrivacidade) == 1:
            amigo = False


        if amigo == False:
            print("\nO usuário que postou o tópico está com o modo de privacidade ativo. Apenas amigos podem comentar.\n")
        else:
            idTopico = Topicos.idDoTopico(self, conta)
            filename = f"Topico_{idTopico}_userID({conta.accountNumber}).txt"

            with open(filename, "a", encoding = "utf8") as file:
                if True:
                    comentario = input("Insira um comentário: ")
                    file.write(f"{conta1.username.capitalize()} (ID: {conta1.accountNumber}): {comentario}\n")

            conta1.listaDeComentariosTopicos.append(comentario)
            conta1.arquivosComentariosTopicos.append(filename)
            print("\nComentário postado.")

class GerenciarReceitasETopicos():
    def __init__(self):
        self.comentarios = []
        self.filename = []
    
    def deletarComentarioTopico(self, conta):
    
        if len(conta.listaDeComentariosTopicos) == 0:
            print("\nVocê não tem comentários postados em tópicos.")
            return
        
        self.comentarios = conta.PassarComentariosTopicos()

        self.filename = conta.PassarArquivosDosComentariosTopicos()

        for i in range(len(self.filename)):
            filename = self.filename[i]
            if os.path.isfile(filename):
                for i in range(len(self.comentarios)):
                    texto_antigo = (f"{conta.username.capitalize()} (ID: {conta.accountNumber}): {self.comentarios[i]}\n")
                    GerenciarReceitasETopicos.deletarComentarioNesseArquivo(self, filename, texto_antigo)

        print("\nOs seus comentários em tópicos foram apagados.")

        conta.listaDeComentariosTopicos.clear()
        self.filename.clear()


    def deletarComentarioReceita(self, conta):
    
        if len(conta.listaDeComentariosReceitas) == 0:
            print("\nVocê não tem comentários postados em receitas.")

        self.comentarios = conta.PassarComentariosReceitas()

        self.filename = conta.PassarArquivosDosComentariosReceitas()

        for i in range(len(self.filename)):
            filename = self.filename[i]
            if os.path.isfile(filename):
                for i in range(len(self.comentarios)):
                    texto_antigo = (f"{conta.username.capitalize()} (ID: {conta.accountNumber}): {self.comentarios[i]}\n")
                    GerenciarReceitasETopicos.deletarComentarioNesseArquivo(self, filename, texto_antigo)

        print("\nOs seus comentários em receitas foram apagados.")

        conta.listaDeComentariosReceitas.clear()
        self.filename.clear()

    def ApagarArquivoReceita(self, conta):
        if conta.idReceita == 1:
            print("\nVocê não tem receitas postadas.")
            return

        self.filename = conta.listaDeReceitas
        for i in range(len(conta.listaDeReceitas)):
            id = f"{conta.accountNumber}{i + 1}"
            Receitas.atualizarAvaliacoesReceitaDeletada(self, id)

        for i in range(len(self.filename)):
            filename = self.filename[i]
            os.remove(filename)

        
        print("\nTodas as receitas postadas por você foram apagadas.")

        conta.listaDeReceitas.clear()
        self.filename.clear()

        Sistema.apagarAvaliacoes(self, conta)
        conta.idReceita = 1


    def ApagarArquivoTopico(self, conta):
    
        if conta.idTopico == 1:
            print("\nVocê não tem tópicos postados.")
            return

        self.filename = conta.listaDeTopicos
        conta.idTopico = 1

        for i in range(len(self.filename)):
            filename = self.filename[i]
            os.remove(filename)

        print("\nTodos os tópicos postados por você foram apagados.")
        conta.listaDeTopicos.clear()
        self.filename.clear()

    def apagarComentarioNaPropriaReceita(self, contaComentarista, conta):
        receitaEncontrada = False

    
        if conta.idReceita == 1:
            print("\nVocê não tem receitas postadas.")
            return

        idReceita = Receitas.idDaReceita(self, conta)
        filename = (f"Receita_{idReceita}_userID({conta.accountNumber}).txt")

        for i in range(len(contaComentarista.arquivosComentariosReceitas)):
            if filename != contaComentarista.arquivosComentariosReceitas[i]:
                receitaEncontrada = False
            else:
                receitaEncontrada = True
        
        if receitaEncontrada == False and conta.accountNumber == contaComentarista.accountNumber:
            print("\nVocê não comentou nessa receita.")
        elif receitaEncontrada == False:
            print("\nEsse usuário não tem comentários postados nessa receita.")
            return
        
        self.comentarios = contaComentarista.listaDeComentariosReceitas

        for i in range(len(contaComentarista.listaDeComentariosReceitas)):
            textoAntigo = (f"{contaComentarista.username.capitalize()} (ID: {contaComentarista.accountNumber}): {self.comentarios[i]}\n")
            GerenciarReceitasETopicos.deletarComentarioNesseArquivo(self, filename, textoAntigo)
        
        print("\nOs comentários desse usuário nessa receita foram apagados.")

        self.comentarios.clear()

    def apagarComentarioNoProprioTopico(self, contaComentarista, conta):
        topicoEncontrado = False

        if conta.idTopico == 1:
            print("\nVocê não tem tópicos postados.")
            return

        idTopico = Topicos.idDoTopico(self, conta)
        filename = (f"Topico_{idTopico}_userID({conta.accountNumber}).txt")

        if filename not in contaComentarista.arquivosComentariosTopicos:
            topicoEncontrado = False
        else:
            topicoEncontrado = True

        if topicoEncontrado == False and conta.accountNumber == contaComentarista.accountNumber:
            print("\nVocê não comentou nesse tópico.")
            return
        elif topicoEncontrado == False:
            print("\nEsse usuário não tem comentários postados nesse tópico.")
            return
        
        self.comentarios = contaComentarista.listaDeComentariosTopicos

        for i in range(len(contaComentarista.listaDeComentariosTopicos)):
            textoAntigo = (f"{contaComentarista.username.capitalize()} (ID: {contaComentarista.accountNumber}): {self.comentarios[i]}\n")
            GerenciarReceitasETopicos.deletarComentarioNesseArquivo(self, filename, textoAntigo)

        print("\nOs comentários desse usuário nesse tópico foram apagados.")

        self.comentarios.clear()

    
    def filtroDeReceitas(self, filename, palavraProcurada, conteudoEscritoNaReceita):
        with open(filename, 'r', encoding = "utf8") as file:
            conteudo = file.read()

            if palavraProcurada.upper() in conteudo.upper() and palavraProcurada.upper() in conteudoEscritoNaReceita.upper():
                return True
            
    def filtroDeTopicos(self, filename, palavraProcurada, conteudoEscritoNoTopico):
        with open(filename, 'r', encoding = "utf8") as file:
            conteudo = file.read()

            if palavraProcurada.upper() in conteudo.upper() and palavraProcurada.upper() in conteudoEscritoNoTopico.upper():
                return True
            
    
    def visualizarTopico(self, conta1):
        amigo  = True
        conta = Topicos.contaDeQuemPostouOTopico(self)

        if conta == False:
            return
        
        if conta.idTopico == 1 and conta1.accountNumber == conta.accountNumber:
            print("\nVocê não tem tópicos postados.")
            return

        if conta.idTopico == 1:
            print("\nEsse usuário não tem tópicos postados.")
            return
        
        if len(conta.usuariosBloqueados) > 0:
            if conta1.username in conta.usuariosBloqueados:
                print("\nVocê não pode visualizar os tópicos desse usuário. Você está bloqueado.")
                return

        
        if int(conta.modoPrivacidade) == 1:
            for i in range(len(conta.listaDeAmigos)):
                if conta1.username != conta.listaDeAmigos[i]:
                    amigo = False
                else:
                    amigo = True
            
        if len(conta.listaDeAmigos) == 0 and int(conta.modoPrivacidade) == 1:
            amigo = False


        if amigo == False:
            print("\nO usuário que postou o tópico está com o modo de privacidade ativo. Apenas amigos podem visualizar.\n")
        else:
            idTopico = Topicos.idDoTopico(self, conta)
            filename = f"Topico_{idTopico}_userID({conta.accountNumber}).txt"

            print(f"\n------TÓPICO {idTopico}------\n")

            with open(filename, 'r', encoding = "utf8") as file:
                conteudo = file.read()
                print(conteudo)

    def visualizarReceita(self, conta1):
        amigo = True

        conta = Receitas.contaDeQuemPostouAReceita(self)
       
        if conta == False:
            return
        
        if conta.idReceita == 1 and conta1.accountNumber == conta.accountNumber:
            print("\nVocê não tem receitas postadas.")
            return

        if conta.idReceita == 1:
            print("\nEsse usuário não tem receitas postadas.")
            return

        if len(conta.usuariosBloqueados) > 0:
            for i in range(len(conta.usuariosBloqueados)):
                if conta1.username == conta.usuariosBloqueados[i]:
                    print("\nVocê não pode visualizar as receitas desse usuário. Você está bloqueado.")
                    return

        if int(conta.modoPrivacidade) == 1:
            for i in range(len(conta.listaDeAmigos)):
                if conta1.username != conta.listaDeAmigos[i]:
                    amigo = False
                else:
                    amigo = True
            
        if len(conta.listaDeAmigos) == 0 and int(conta.modoPrivacidade) == 1:
            amigo = False
        
        if conta.accountNumber == conta1.accountNumber:
            amigo = True

        if amigo == False:
            print("\nO usuário que postou a receita está com o modo de privacidade ativo. Apenas amigos podem visualizar.\n")
        else:
            idReceita = Receitas.idDaReceita(self, conta)
            filename = f"Receita_{idReceita}_userID({conta.accountNumber}).txt"

            print(f"\n------RECEITA {idReceita}------\n")

            with open(filename, 'r', encoding = "utf8") as file:
                conteudo = file.read()
                print(conteudo)
                
        
            

        

    def usernameComentario(self, conta, topicoOuReceita):
        accountNumber = Sistema.verificarNumeroDaConta(self, 6)
        contaComentarista = Sistema.username(self, accountNumber)
        if topicoOuReceita == 1:
            GerenciarReceitasETopicos.apagarComentarioNoProprioTopico(self, contaComentarista, conta)
        else:
            GerenciarReceitasETopicos.apagarComentarioNaPropriaReceita(self, contaComentarista, conta)


    def deletarComentarioNesseArquivo(self, filename, comentario):
        with open(filename, 'r', encoding = 'utf8') as file:
            conteudo = file.read()

        conteudoModificado = conteudo.replace(f"{comentario}", '')

        with open(filename, 'w', encoding = "utf8") as file:
            file.writelines(conteudoModificado)

login = Sistema()