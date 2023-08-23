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
