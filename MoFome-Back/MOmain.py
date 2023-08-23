import os
from account import *
from subscriptions import *
from messages import *
from gerenciarRecipes import *
from topics import *
from recipeFeedback import *
from recipes import *
from editAccout import *

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

login = Sistema()

print("\n------")
print("MoFome")
print("------\n")

while True:

    print ("\nDigite 1 para criar uma conta.") 
    print ("Digite 2 logar na sua conta.")
    print ("Digite 3 para recuperar o seu ID.")
    print ("Digite 4 para recuperar o seu nome de usuário.")
    print ("Digite 20 para encerrar o programa.")


    action = input("\nInsira a opção: ")

    if action == '1':
        login.abrirConta()

    if action == '2':
        checarSeEncerra = login.logarNaConta()
        if checarSeEncerra == False:
            break

    if action == '3':
        login.recoverID()
    
    if action == '4':
        login.accountRecovery()

    if action == '20':
        break