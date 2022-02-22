from turtle import color
import PySimpleGUI as sg
from numpy import tile

sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#ADD8E6',
                                        'TEXT': '#000000',
                                        'INPUT': '#FFFFFF',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL': '#99CC99',
                                        'BUTTON': ('#003333', '#FFCC66'),
                                        'PROGRESS': ('#D1826B', '#CC8019'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 
'PROGRESS_DEPTH': 0, }

sg.theme('MyCreatedTheme')

resultado = 0

title = [
    [sg.Text('CALCULO REGRA DE 3 - TESTE')]
]

coluns_ok_cancel = [
    [sg.Button('Calcular', button_color='#32CD32', size=(20, 1)),
    sg.Button('Cancelar', size=(10, 1))]
]

layout = [
    [sg.Column(title, vertical_alignment='center', justification='c')],
    [sg.Text('Valor'), sg.InputText(size=(10,5)), sg.Text('---'), sg.InputText(size=(10,5)), sg.Text('Valor')],
    [sg.Text('Valor'), sg.InputText(size=(10,5)), sg.Text('---'), sg.InputText(size=(10,5)), sg.Text('Valor')],
    [sg.Column(coluns_ok_cancel, vertical_alignment='center', justification='c')]
]

window = sg.Window('Regra de 3', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    elif event == 'Calcular':
        try:
            resultado = int(values[0]) + int(values[1])
            resultado2 = int(values[2]) + int(values[3])
            sg.popup_ok(f'Resultado: {resultado} / {resultado2}')
        except ValueError:
            sg.popup_error('Entre com valores númericos!')
window.close()
