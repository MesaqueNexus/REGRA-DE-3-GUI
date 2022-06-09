# ** conding: UTF-8 **
# By Mesaque Nexus
# Python 3

import PySimpleGUI as sg

# Criar um novo tema
sg.LOOK_AND_FEEL_TABLE['Nexus'] = {'BACKGROUND': '#ADD8E6',
                                        'TEXT': '#000000',
                                        'INPUT': '#FFFFFF',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL': '#99CC99',
                                        'BUTTON': ('#003333', '#FFCC66'),
                                        'PROGRESS': ('#D1826B', '#CC8019'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0, 
                                    }

# Aplica o Tema Criado 
sg.theme('Nexus')

# Colunas do Layout
title = [
    [sg.Text('CALCULO REGRA DE 3')]
]

x = [
    [sg.Text('X', pad=(0, 0))]
]

coluna_valor_01 = [
    [sg.Text('Valor'), sg.InputText(size=(10,5), key='Valor01')],
    [sg.Column(x, vertical_alignment='center', justification='c')]
]

coluna_valor_02 = [
    [sg.InputText(size=(10,5), key='Valor02'), sg.Text('Valor')],
    [sg.InputText(size=(10,5), key='Valor03'), sg.Text('Valor')]
]

coluns_ok_cancel = [
    [sg.Button('Calcular', button_color='#32CD32', size=(20, 1)),
    sg.Button('Cancelar', size=(10, 1))]
]

coluna_separadores = [
    [sg.Text('-----')],
    [sg.Text('-----')]
]

# Layout Principal
layout = [
    [sg.Column(title, vertical_alignment='center', justification='c')],
    [sg.Column(coluna_valor_01), sg.Column(coluna_separadores) ,sg.Column(coluna_valor_02)],
    [sg.Column(coluns_ok_cancel, vertical_alignment='center', justification='c')],
    [sg.Text('©MesaqueNexus™', pad=(0, 0))]
]

# Parte Lógica
window = sg.Window('Regra de 3', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    elif event == 'Calcular':
        try:
            calculo = (int(values['Valor01']) * int(values['Valor03'])) / int(values['Valor02'])
            sg.popup_ok(f'Resultado:\n{calculo}')
        except ValueError:
            sg.popup_ok('Entre com valores númericos!')
window.close()
