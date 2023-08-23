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