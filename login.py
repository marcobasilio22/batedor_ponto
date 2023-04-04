import PySimpleGUI as sg
from PySimpleGUI import theme
from horario import horarios
from layout import corpo, user
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.get_database("Ponto")
collection = db.get_collection("Usuários")

theme('DarkGray')

def t_login():

    layout=[
        [sg.Text('Usuário')],
        [sg.Input(key='usuario')],
        [sg.Text('senha')],
        [sg.Input(key='senha', password_char='**')],
        [sg.Button('login')],
        [sg.Text('', key='menssagem')],
    ]

    janela = sg.Window('Login', layout, finalize=True) 

    while True:
        event, values = janela.read()
        if event ==  sg.WIN_CLOSED:
            break 
        elif event == 'login':
            user
            s_correta = '123'
            usuario = values['usuario']
            senha = values['senha']
            
            if senha == s_correta and usuario == user:
                janela.close()
            else:
                janela['menssagem'].update('Senha ou usuário incorreto')

            if collection.find_one({"USUARIO": usuario}) is None:
                dados = {"USUARIO": usuario,
                          "SENHA": senha}
                collection.insert_one(dados)
            else:
                print("Os dados já existem no MongoDB!")

t_login()
from estrutura import Iniciar