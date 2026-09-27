# %%

idades =[
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

idades

media = sum(idades) / len(idades)
print("Média", media)

diffs = 0 

for i in idades:
    diffs += (i - media) ** 2

variancia = diffs / (len(idades)-1)

print("Variância", variancia)

#nós fazemos essas estatísticas na mão pois o python não tem, nativamente, métodos para as listas para calcular média, variância e outros cálculos estatísticos

# %%
#por isso nós vamos utilizar o pandas, que é uma biblioteca específica para esse tipo de situação:

import pandas as pd

#além disso, utilizando o pandas nós vamos ser apresentados às "Series", que são estruturas de dados melhores para trabalharmos os dados e calcularmos as estatísticas:

idades =[
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

series_idades = pd.Series(idades)
series_idades

#Uma diferença interessante entre as Series e as listas é que nas Series, é importante trabalhar apenas com um tipo de dado. Além disso, as Series já tem métodos aplicáveis que facilitam a nossa vida para calcular as estatísticas

# %%

#Uma diferença interessante entre as Series e as listas é que nas Series, é importante trabalhar apenas com um tipo de dado. Além disso, as Series já tem métodos aplicáveis que facilitam a nossa vida para calcular as estatísticas:

#Método .mean() para calcular média
media_idades = series_idades.mean()

#método .var() para calcular variância
var_idades = series_idades.var()

#método .describe() para ver um resumo estatístico da Serie com vários cálculos como média, desvio padrão, mediana etc...
summary_idades = series_idades.describe()

print("Média:", media_idades)
print("Variância", var_idades)
print("Sumário Estatísticas \n", summary_idades)

# %%


