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
        