class Account():
    def __init__(self, name, password, username, accountNumber): 
        self.listaDeAmigos = []
        self.listaDeReceitas = []
        self.recipeDictID = 0
        self.recipeDict = {}
        self.listaDeTopicos = []
        self.arquivosComentariosTopicos = []
        self.arquivosComentariosReceitas = []
        self.listaDeComentariosReceitas = []
        self.listaDeComentariosTopicos = []
        self.listaDeReceitasAvaliadas = []
        self.listaDeMensagens = []
        self.listaDeMensagensNaoLidas = []
        self.dictAvaliacoesRecebidas = {}
        self.arquivosDeChat = []
        self.listaDeQuemEstaSeguindo = []
        self.listaDeSeguidoresUsername = []
        self.listaDeSeguidores = []
        self.listaDeNotificacoesDeInscricoes = []
        self.conteudoEscritoNaReceita = []
        self.conteudoEscritoNoTopico = []
        self.mensagensFeitas = []
        self.name = name
        self.__password = password
        self.username = username
        self.__accountNumber = accountNumber
        self.idReceita = 1
        self.idTopico = 1
        self.modoPrivacidade = 0
        self.usuariosBloqueados = []

    def AtivarPrivacidade(self):
        self.modoPrivacidade = 1
        print("\nModo de privacidade está ativado.\n")

    def DesativarPrivacidade(self):
        self.modoPrivacidade = 0
        print("\nModo de privacidade está desativado.\n")

    def ChecarSenha(self, password):
        while True:
            try:
                if password != self.__password:
                    raise ValueError("Senha incorreta.")
                else:
                    break
                
            except ValueError as e:
                print(e)
                password = input("Insira a senha novamente: ")
    

    def show(self):
        print(f"\nNome: {self.name}")
        print(f"Senha: {self.__password}")
        print(f"Nome de usuário: {self.username}")

        if self.modoPrivacidade == 1:
            print(f"Modo de privacidade está ativado.")
        else:
            print(f"Modo de privacidade está desativado")

        print(f"Quantidade de receitas postadas: {self.idReceita - 1}")
        print(f"Quantidade de tópicos postados: {self.idTopico - 1}")
        print(f"Quantidade de comentários em tópicos: {len(self.listaDeComentariosTopicos)}")
        print(f"Quantidade de comentários em receitas: {len(self.listaDeComentariosReceitas)}")
        
        
        Account.showBloqueados(self)
        Account.showFriends(self)

    def showOutroUser(self):
        print(f"\nNome: {self.name}")
        print(f"Senha: {self.password}")
        print(f"Nome de usuário: {self.username}")
        print(f"Quantidade de receitas postadas: {self.idReceita - 1}")
        print(f"Quantidade de tópicos postados: {self.idTopico - 1}")
        print(f"Quantidade de comentários em tópicos: {len(self.listaDeComentariosTopicos)}")
        print(f"Quantidade de comentários em receitas: {len(self.listaDeComentariosReceitas)}")


    def showBloqueados(self):
        if len(self.usuariosBloqueados) > 0:
            print("Usuários bloqueados: ", end = "")
            for i in range(len(self.usuariosBloqueados) - 1):
                print(f"{self.usuariosBloqueados[i]}, ", end = "")
            print(f"{self.usuariosBloqueados[(len(self.usuariosBloqueados)) - 1]}.")
        else:
            print("Você não tem usuários bloqueados.")
    
    def showFriends(self):
        if len(self.listaDeAmigos) > 0:
            print("Amigos: ", end = "")
            for i in range(len(self.listaDeAmigos) - 1):
                print(f"{self.listaDeAmigos[i]}, ", end = "" )
            print(f"{self.listaDeAmigos[(len(self.listaDeAmigos)) - 1]}.\n")
        else:
            print("Você não tem amigos.\n")

    def verMensagens(self):
        if len(self.listaDeMensagens) > 0:
            print("Mensagens recebidas: ")
            for i in range(len(self.listaDeMensagens) - 1):
                print(f"{self.listaDeMensagens[i]}\n")
            print(f"{self.listaDeMensagens[(len(self.listaDeMensagens)) - 1]}")
        else:
            print("Você não tem mensagens recebidas.")

    def verMensagensNaoLidas(self):
        if len(self.listaDeMensagensNaoLidas) > 0:
            print("Novas mensagens: ")
            for i in range(len(self.listaDeMensagensNaoLidas) - 1):
                print(f"{self.listaDeMensagensNaoLidas[i]}\n ")
            print(f"{self.listaDeMensagensNaoLidas[(len(self.listaDeMensagensNaoLidas)) - 1]}")
            self.listaDeMensagensNaoLidas.clear()
        else:
            print("\nVocê não tem mensagens novas.")
    
    def inscricoes(self):
        print("\n")
        if len(self.listaDeNotificacoesDeInscricoes) > 0:
            for notificacao in self.listaDeNotificacoesDeInscricoes:
                print(notificacao)
        else:
            print("\nNenhuma notificação nova.")
        
        self.listaDeNotificacoesDeInscricoes.clear()
    
    def mostrarQuemEstaSeguindo(self):
        print("\n")
        if len(self.listaDeQuemEstaSeguindo) > 0:
            print("Seguindo: ", end = "")
            for i in range(len(self.listaDeQuemEstaSeguindo) - 1):
                print(f"{self.listaDeQuemEstaSeguindo[i]}, ", end = "" )
            print(f"{self.listaDeQuemEstaSeguindo[(len(self.listaDeQuemEstaSeguindo)) - 1]}.\n")
        else:
            print("Você não está seguindo alguém.\n")

    def listaReceitas(self, filename):
        self.listaDeReceitas.append(filename)
        self.idReceita = self.idReceita + 1
        print("\nReceita postada.")

    def listaTopicos(self, filename):
        self.listaDeTopicos.append(filename)
        self.idTopico = self.idTopico + 1
        print("\nTópico postado.")

    def ComentariosTopicos(self, comentario, filename):
        self.listaDeComentariosTopicos.append(comentario)
        self.arquivosComentariosTopicos.append(filename)
        print("\nComentário postado.")

    
    def PassarComentariosTopicos(self):
        comentarios = self.listaDeComentariosTopicos
        return comentarios
        
    def PassarArquivosDosComentariosTopicos(self):
        filename = self.arquivosComentariosTopicos
        return filename
    
    def PassarComentariosReceitas(self):
        comentarios = self.listaDeComentariosReceitas
        return comentarios
    
    def PassarArquivosDosComentariosReceitas(self):
        filename = self.arquivosComentariosReceitas
        return filename
    
    def getAccountNumber(self):
        return self.__accountNumber
    
    def getPassword(self):
        return self.__password
    
    def passwordSetter(self, newPassword):
        self.__password = newPassword