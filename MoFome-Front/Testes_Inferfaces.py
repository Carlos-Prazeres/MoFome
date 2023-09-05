from PySimpleGUI import PySimpleGUI as sg

#Layout 
sg.theme ('DarkAmber')

layout_start = [
    [sg.Image (r'C:\Users\carlo\OneDrive\Área de Trabalho\Projetos\Projeto de Software\MoFome\Logo.png')],
    #[sg.Text ('Já possui conta?'), sg.Radio ('Sim', "RADI01"), sg.Radio('Não',"RADI01")]
    [sg.Button('Já possuo conta', key ='ja_tenho_conta'), sg.Button('Quero ter criar uma conta', key = 'criar_conta')]
]


layout_imput_user = [
    [sg.Text ('Usuário'), sg.Input(key = 'usuario')],
    [sg.Text ('Senha  '), sg.Input(key = 'senha', password_char = '*')],
    [sg.Text ('Seu id:'), sg.Input(key = 'id', password_char = '*')],
    [sg.Checkbox ('Salvar o login?')],
    [sg.Button('Entrar')]
]

layout_create_user = [
    [sg.Text('Digite seu nome:'), sg.Input(key = 'name')],
    [sg.Text('Crie uma senha'), sg.Input(key = 'password')],
    [sg.Text('Crie um nome de usuário'), sg.Input(key = 'username')],
    [sg.Button('Criar conta')]
]
#Janela 
janela = sg.Window ('MoFome', layout_start)

#ler os eventos
'''while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Entrar":
        if valores['usuario'] == 'Jonatan' and valores['senha'] == '123456':
            print ('Bem-vindo')
        else:
            print ('Senha incorreta')'''


def entrada_de_login ():
    janela_de_login = sg.Window ('MoFome', layout_imput_user)
    dados = janela_de_login.read()

def criar_um_login ():
    janela_de_criar_conta = sg.Window ('MoFome', layout_create_user)
    dados = janela_de_criar_conta.read()
    while True:
        if dados == sg.WINDOW_CLOSED:
            break
        elif eventos == "Criar conta":
            break

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == "ja_tenho_conta":
        janela.close()
        entrada_de_login ()
    elif eventos == "criar_conta":
        janela.close()
        criar_um_login()

