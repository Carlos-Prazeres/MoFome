import os
from MOmain import Sistema

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