import PySimpleGUI as sg
import random

def gerar_numero_aleatorio():
    return random.randint(1, 10)

layout = [
    [sg.Text('Digite um número de 1 a 10:'), sg.Input(key='-NUM-')],
    [sg.Button('Verificar')],
    [sg.Text('', size=(30, 1), key='-RESULTADO-')]
]

janela = sg.Window('Gerador de Números Aleatórios').Layout(layout)

while True:
    evento, valores = janela.Read()

    if evento == sg.WIN_CLOSED:
        break

    if evento == 'Verificar':
        try:
            num_digitado = int(valores['-NUM-'])
            num_aleatorio = gerar_numero_aleatorio()

            if num_digitado == num_aleatorio:
                mensagem = 'Você acertou!'
            else:
                mensagem = 'Você errou! O número era {}'.format(num_aleatorio)

            janela['-RESULTADO-'].update(mensagem)

        except ValueError:
            sg.popup_error('Por favor, digite um número válido.')

janela.close()
