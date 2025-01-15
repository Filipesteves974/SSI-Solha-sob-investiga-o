import pandas as pnd
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

Mlin = -0.015071678245297768
Blin = 1.154870981763541
Mlog = -0.1949
Blog = 8.0617


def logistic_regr(m, b, x):
    y = (math.e) ** (m * x + b) / (1 + (math.e) ** (m * x + b))
    return y

def erro(y, y1):
    erros = []
    for i, j in zip(y, y1):
        erros.append(abs(i - j))
    return erros

def main():
    data = pnd.read_excel
    solea = data['solea'].values
    mud = data['mud'].values
    r = lambda x: Mlin * x + Blin
    s = lambda x: logistic_regr(Mlog, Blog, x)
    solea_r = [r(i) for i in mud]
    solea_s = [s(i) for i in mud]
    e1 = erro(solea, solea_r)
    e2 = erro(solea, solea_s)
    plt.figure(figsize=(8, 6), dpi=(300))
    rect = patches.Rectangle((34.28, -0.1), 16.44, 1.2, alpha=0.2, facecolor='k',
    label ='Zona de Ausência / Presença Simultânea')
    plt.gca().add_patch(rect)
    plt.plot(mud, e2, 'r -', label ='Regr.Logística')
    plt.plot(mud, e1, 'b–', label ='Regr.Linear')
    plt.axis([0, 100, -0.1, 1.1])
    plt.ylabel('Erro Absoluto')
    plt.xlabel('Percentagem de Argila( %)')
    plt.legend()
    plt.show()

main()
