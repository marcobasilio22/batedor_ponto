import PySimpleGUI as sg
from PySimpleGUI import theme
from horario import horarios
from layout import corpo
import pymongo
from relatorio import r_pdf
import webbrowser


client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.get_database("Ponto")
collection = db.get_collection("Registros")

theme('DarkGrey4')

janela = sg.Window("Ponto", corpo())

def Iniciar():

    while True:
        event, values = janela.read(timeout=60)
        if event == sg.WIN_CLOSED:
            break
        if event == 'Relatório':
            r_pdf()
            webbrowser.open("relatorio.pdf")
        janela['-TIME-'].update(horarios())
        if callable (event):    
            event()

Iniciar()
