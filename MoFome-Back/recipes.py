from MOmain import Sistema
from recipeFeedback import AvaliacaoDeReceitas


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