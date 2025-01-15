import pandas as pnd
import matplotlib.pyplot as plt
import numpy as np
import math
import statsmodels.api as sm
import statsmodels.formula.api as smf


def logistic_regr(m, b, x):
    y = (math.e) ** (m * x + b) / (1 + (math.e) ** (m * x + b))
    return y


def main():
    data = pnd.read_excel
    solea = data['solea'].values
    mud = data['mud'].values
    formula = 'solea mud'
    model = smf.glm(formula=formula, data=data, family=sm.families.Binomial())
    result = model.fit()
    print(result.summary())
    df = pnd.read_html(result.summary().tables[1]._as_html(), header = 0,index_col = 0)[0]
    m = df['coef'].values[1]
    b = df['coef'].values[0]
    f = lambda x: logistic_regr(m, b, x)
    xdata = np.linspace(1, 100, 100)
    ydata = f(xdata)
    plt.figure(figsize=(8, 6), dpi=(300))
    plt.plot(mud, solea, 'ko')
    plt.plot(xdata, ydata, 'r–')
    plt.axis([0, 100, -0.1, 1.1])
    plt.ylabel('Presença / Ausência de Solha')
    plt.xlabel('Percentagem de Argila(%)')
    plt.show()
    print('Eq. da Regressão Logística do tipo:')
    print('y = exp_z / (1 + exp z) \n')
    print("z =", m, 'end=')
    print("x +", b)

main()