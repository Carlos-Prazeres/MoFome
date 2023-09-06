accountsList = []

def newAccount(aName, aPassword, aUser):
    global accountsList
    friendList = []
    newAccountDict = {'nome':aName, 'senha':aPassword, 'user':aUser, 'friends' :friendList}
    accountsList.append(newAccountDict)
def show(accountNumber):
    global accountsList
    print('Conta', accountNumber)
    thisAccountDict = accountsList[int (accountNumber)]
    #print('       Nome', thisAccountDict['nome'])
    print('       Senha:', thisAccountDict['senha'])
    print('       Nome de Usuário:', thisAccountDict['user'])
    friendList = thisAccountDict['friends']
    print ("       Seguindo:")
    for i in range (len(friendList)):
        print ('              ' + friendList[i])
    print()
def accountRecovery(accountNumber):
    global accountsList
    thisAccountDict = accountsList[int(accountNumber)]
    print('Sua senha é:', thisAccountDict['senha'])
def changeProfile(newPassword, newUser, accountNumber):
    global accountsList
    thisAccountDict = accountsList[int(accountNumber)]
    thisAccountDict['senha'] = newPassword
    thisAccountDict['user'] = newUser

def postManagement(accountNumber):
    global accountsList
    thisAccountDict = accountsList[int(accountNumber)]
    filename = f"{thisAccountDict['user']}.txt"
    with open(filename, "w") as file:
        if True:
            receita = input("")
            file.writelines(receita)
    print('Sua receita foi criada')

def addFriends(accountNumber):
    global accountsList
    print('Digite o id de quem você deseja adicionar')
    newFriend = input("")
    thisAccountDict = accountsList[int(accountNumber)]
    friendAccountDict = accountsList[int(newFriend)]
    thisAccountDict['friends'].append(friendAccountDict['user'])

#print ('Momesso é usúario da MoFome e seu id é', len(accountsList))
#print ("\n")
#newAccount("lucas", 1234, "Momesso")

print ("Olá, Bem Vindo(a) ao MoFOme, a sua rede de fanáticos gastronômicos\n")

while True:
    print ("Digite 1 para criar uma conta") #newAccount
    print ("Digite 2 para editar a sua conta") #changeProfile
    print ("Digite 3 para adicionar pessoas para seguir")
    print ("Digite 4 para postar uma receita") #postmanagement
    print ("Digite 5 para recuperar a sua conta") #accountRecovery
    print ("Digite 7 para ver o seu perfil") #show
    #print ("Digite 8 para ver o seu feed") 
    print ("Digite 9 para sair")

    action = input("Qual a sua opcao?")

    if action == '1':
        new_name = input ("Qual o seu Nome?\n")
        new_name = new_name.lower()
        new_password = input ("Qual será a sua senha?\n")
        new_user = input ("Digite um nome de usuário:")
        new_user = new_user.lower()
        newAccount(newAccount, new_password, new_user)
        accout_number = int (len(accountsList) - 1)
        print ('Seu id é o número', accout_number)
        print ("Conta Criada\n")

    if action == '2':
        user = input ("Digite sua novo nome:\n")
        passoword = input ("Digite seu nova senha:\n")
        id_alterar = input ("Digite seu id:")
        changeProfile (passoword, user, id_alterar)

        print ("Conta editada\n")
    
    if action == '3':
        id_frend = input ("Qual o seu id:\n")
        addFriends (id_frend)
        print ("Seguindo\n")
    
    if action == '4':
        id_recipe = input ("Digite seu id:\n")
        postManagement(id_recipe)
        print ("Receita postada\n") #cria um txt com a receita
    
    if action == '5':
        id_atual = input ("Digite seu id:\n")
        accountRecovery(id_atual)
        print ("Conta recuperada\n")

    if action == '7':
        id_Show = input ("Qual o seu id?\n")
        show(id_Show)
        thisAccountDict = accountsList[int (id_Show)]
        user_show = thisAccountDict['user']
        
        #print ("Seu post foi:\n")

        #arquivo = open(f"{user_show}.txt", "r")
        #print (arquivo.readlines())
        #print (arquivo.readlines())
        #print (user_show)

    if action == '9':
        print ("Até mais!!")
        break
        
