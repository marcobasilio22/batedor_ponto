import PySimpleGUI as sg
from PySimpleGUI import Push, Column, VSeparator, theme
from horario import f_data, horarios
import pymongo

theme('DarkGreen3')

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.get_database("Ponto")
collection = db.get_collection("Registros")


parar_botao1 = False
parar_botao2 = False
parar_botao3 = False
parar_botao4 = False

user = 'Marco'                                                                      #Usuário


def b1(op):
    global parar_botao1
    if op == 1 and parar_botao1 == False:
        print(f"Inicio de jornada {horarios()}")
        parar_botao1 = True
        dado = {"USUARIO": user,
                "HORARIO_INICIO": horarios(),
                "DATA": f_data()}
        collection.insert_one(dado)
    elif op == 1 == parar_botao1 == True:
        False

    
def b2(op):
    global parar_botao2
    if op == 2 and parar_botao2 == False:
        print(f"Pausa almoço {horarios()}")
        parar_botao2 = True
        dado = {"USUARIO": user,
                "INICIO_ALMOÇO": horarios(),
                "DATA": f_data()}
        collection.insert_one(dado)

    elif op == 2 and parar_botao2 == True:
        print(f"Retorno almoço {horarios()}")
        parar_botao2 = False
        dado = {"USUARIO": user,
                "RETORNO_ALMOÇO": horarios(),
                "DATA": f_data()}
        collection.insert_one(dado)


def b3(op):
    global parar_botao3
    if op == 3 and parar_botao3 == False:
        print(f"Pausa {horarios()}")
        parar_botao3 = True
        dado = {"USUARIO": user,
                "INICIO_PAUSA": horarios(),
                "DATA": f_data()}
        collection.insert_one(dado)

    elif op == 3 and parar_botao3 == True:
        print(f"Retorno {horarios()}")
        parar_botao3 = False
        dado = {"USUARIO": user,
                "RETORNO_PAUSA": horarios(),
                "DATA": f_data()}
        collection.insert_one(dado)

def b4(op):
    global parar_botao4
    if op == 4 and parar_botao4 == False:
        print(f"Fim de jornada {horarios()}")
        parar_botao4 = True
        dado = {"USUARIO": user,
                "HORARIO_ENCERRAMENTO": horarios(),
                "DATA": f_data()}
        collection.insert_one(dado)
    elif op == 4 == parar_botao1 == True:
        False
    

botao1 = sg.Button('Inicio', key=lambda: b1(1), size=(10,7))
botao2 = sg.Button('Almoço', key=lambda: b2(2), size=(10,7))
botao3 = sg.Button('Pausa', key=lambda: b3(3), size=(10,7))
botao4 = sg.Button('Fim',key=lambda: b4(4), size=(10,7))


def corpo():

    esquerda = [
            
        [sg.Text(user, font=("Arial", 20)),                                         #Nome                                            
        sg.Text(f_data(), font=("Arial", 20))],                                     #Data
            
        [Push(),Push(), Push(),
        sg.Text('', key='-TIME-' ,font=("Arial", 15)),                              #Hora                           
        Push()],

        [sg.Canvas(size=(50,50), key='canvas')],

        [botao1,                                                    
        sg.Canvas(size=(10,10), key='canvas'),                 
        botao2],
        
        [sg.Canvas(size=(10,10), key='canvas')],               

        [botao3,                          
        sg.Canvas(size=(10,10), key='canvas'),                
        botao4]                   
        ]

    direita = [
        [sg.Output(size=(30,20)),
        sg.Button('Relatório',size=(6,1), pad=((0,0),(400,0)))]]

        

    layout = [
        [Column(esquerda), VSeparator(), Column(direita)  ]    
        ]
    return layout

