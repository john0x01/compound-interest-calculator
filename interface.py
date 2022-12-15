from PySimpleGUI import PySimpleGUI as pg
from graph import main
import json

class Tela:
    def __init__(self):
        global window

        # Layout
        pg.theme('Reddit')
        layout = [
            [pg.Text('Valor Inicial:', size=(18, 1))],
            [pg.Input(key='initialValue', size=(40, 2))],
            [pg.Text('Aporte Mensal:', size=(18, 1))],
            [pg.Input(key='contribution', size=(40, 2))],
            [pg.Text('Período:')],
            [pg.Input(key='period', size=(40, 2)), pg.Combo(['months', 'years'], key='periodMeasurement')],
            [pg.Text('Taxa (%)')],
            [pg.Input(key='interest', size=(40, 2)), pg.Combo(['monthly', 'yearly'], key='interestMeasurement')],
            [pg.Button('Calcular', key='calc',size=(40, 2))]
        ]

        # Window
        window = pg.Window('Calculadora de juros', layout)

        # Read Events
        self.event, self.values = window.read()
        if self.event == pg.WIN_CLOSED or self.event == 'Quit':
            exit()

    def simulate(self):

        # Get variables
        initialValue = float(self.values['initialValue'])
        contribution = float(self.values['contribution'])
        periodMeasurement = self.values['periodMeasurement']
        interestMeasurement = self.values['interestMeasurement']
        period = int(self.values['period'])
        interest = float(1 + (float(self.values['interest']) / 100))

        data = {}

        # Send to JSON
        data['values'] = []
        data['values'].append({
            "initialValue": initialValue,
            "contribution": contribution,
            "period": period,
            "interest": interest,
            "periodMeasurement": periodMeasurement,
            "interestMeasurement": interestMeasurement
        })

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
        
        main.calculate()

tela = Tela()
tela.simulate()
