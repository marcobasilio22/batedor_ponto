import PySimpleGUI as sg
from PySimpleGUI import Push, Column, VSeparator
from datetime import datetime, date, time
import locale

def horarios():
    locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil')
    tempo = datetime.now()
    f_horas = tempo.strftime('%X')
    return f_horas

def f_data():
    formatacao = date.today().strftime('%d/%m/%Y')  
    return formatacao