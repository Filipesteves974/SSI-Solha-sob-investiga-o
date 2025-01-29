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
    data = pnd.read_excel('Localização do ficheiro')
    solea = data['solea'].values
    mud = data['mud'].values
    
    m = minimosquadrados(mud, solea)
    media_solea = sum(solea) / len(solea)
    media_mud = sum(mud) / len(mud)
    b = media_solea - m * media_mud
    r = lambda x: m * x + b
    data_X = [1, 100]
    data_Y = [r(data_X[0]), r(data_X[1])]
    
    plt.figure(figsize=(8, 6), dpi=(300))
    plt.plot(mud, solea, 'ko')
    plt.plot(data_X, data_Y, 'r --', label = 'y = -0.0151x + 1.1549')
    plt.axis([0, 100, -0.1, 1.1])
    plt.ylabel('Presença / Ausência de Solha')
    plt.xlabel('Percentagem de Argila(%)')
    plt.legend(loc= 'upper center', bbox_to_anchor= (0.5, -0.05), 
               fancybox = True, shadow = True, ncol = 5)
    plt.show()
    
    print('Eq. da Regressão Linear:')
    print(f'y = {m}x + {b}\n' )
    print('Eq. da Reg.Linear(arredondado a 3 casas décimais):')
    print('y =', round(m, 3), 'x +', round(b, 3))

main()
