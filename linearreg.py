import pandas as pnd
import matplotlib.pyplot as plt


def minimos_quadrados(x, y):
    somay = sum(y)
    somax = sum(x)
    somax2 = sum(x ** 2)
    somaxy = sum(x * y)
    m = (somaxy - somax * somay / 65) / (somax2 - somax ** 2 / 65)
    return m


def main():
    data = pnd.read_excel
    solea = data.loc[0:, ['solea']]
    mud = data.loc[0:, ['mud']]
    solea = data['solea'].values
    mud = data['mud'].values
    m = minimosquadrados(mud_list, solea_list)
    media_solea = sum(solea) / len(solea)
    media_mud = sum(mud) / len(mud)
    b = media_solea - m * media_mud
    r = lambda x: m * x + b
    data_X = [1, 100]
    data_Y = [r(data_X[0]), r(data_X[1])]
    plt.figure(figsize=(8, 6), dpi=(300))
    plt.plot(mud, solea, 'ko')
    plt.plot(data_X, data_Y, 'r-')
    plt.axis([0, 100, -0.1, 1.1])
    plt.ylabel('Presença / Ausência de Solha')
    plt.xlabel('Percentagem de Argila(%)')
    plt.show()
    print('Eq. da Regressão Linear:')
    print(f'y = {m}x + {b}\n' )
    print('Eq. da Reg.Linear(arredondado a 3 casas décimais):')
    print('y =', round(m, 3), 'x +', round(b, 3))

main()