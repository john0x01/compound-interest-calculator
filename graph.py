from matplotlib import pyplot as plt
import json

def sequency(lista, numero):
    for k in range(numero):
        lista.append(k)
    return lista

def formula(months, invested, amount, contribution, interest, interestMeasuremnt):
    n = 0
    profit = 0
    while n != months:
        amount += contribution
        invested += contribution
        if interestMeasuremnt == 'mensal':
            amount = round((amount * interest), 2)
        elif interestMeasuremnt == 'anual':
            if (n % 12) == 0 and n != 0:
                amount = round((amount * interest), 2)

        profit = round((amount - invested), 2)
        n += 1
    return [months, invested, amount, contribution, interest, profit]


class Main:
    def __init__(self):
        with open('data.json') as json_file:
            data = json.load(json_file)
            for p in data['values']:
                self.initialValue = p['initialValue']
                self.contribution = p['contribution']
                self.period = p['period']
                self.interest = p['interest']
                self.periodMeasurement = p['periodMeasurement']
                self.interestMeasurement = p['interestMeasurement']
                
        self.total = self.initialValue
        if self.periodMeasurement == 'anos':
            self.finals = formula(self.period * 12, self.initialValue, self.total, self.contribution, self.interest, self.interestMeasurement)
        elif self.periodMeasurement == 'meses':
            self.finals = formula(self.period, self.initialValue, self.total, self.contribution, self.interest, self.interestMeasurement)
    
    def calculate(self):
        self.x = []
        self.x = sequency(self.x, self.period + 1)

        self.amountGraph = []
        self.investedGraph = []
        self.profitGraph = []

        for n in self.x:
            if self.periodMeasurement == 'anos':
                resultados = formula(n * 12, self.initialValue, self.total, self.contribution, self.interest, self.interestMeasurement)
            elif self.periodMeasurement == 'meses':
                resultados = formula(n, self.initialValue, self.total, self.contribution, self.interest, self.interestMeasurement)

            self.amountGraph.append(resultados[2])
            self.investedGraph.append(resultados[1])
            self.profitGraph.append(resultados[5])
        
        self.graph()
    
    def graph(self):
        plt.plot(self.x, self.profitGraph, 'g-', label='Lucro')
        plt.plot(self.x, self.investedGraph, 'r-', label='Capital Investido')
        plt.plot(self.x, self.amountGraph, 'b-', label='Total')

        profits = self.finals[5]
        lastTotal = self.finals[2]
        invested = self.finals[1]

        plt.legend(loc=9)

        if self.periodMeasurement == 'anos':
            plt.xlabel("Anos")
        elif self.periodMeasurement == 'meses':
            plt.xlabel("Meses")
        plt.ylabel("Reais")
        plt.title(f"Total: R${round(lastTotal, 2)} Investido: R${round(invested, 2)} Lucro: R${round(profits, 2)} ")
        plt.show()

main = Main()
