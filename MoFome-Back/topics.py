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