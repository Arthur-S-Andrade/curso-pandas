# %%

import pandas as pd



# %%

pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]

filtro = []
for i in pontos:
    filtro.append(i>=50)

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i]) 

resultado

# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32,35, 14],
        "uf": ["sp", "pr", "rj"]
    }
)

filtro = brinquedo["idade"] >= 18

brinquedo[filtro]

# %%

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

# %%


filtro = df["QtdePontos"] >= 50

filtro

# %%

#filtro_1 = valores maiores ou iguais a 50
filtro_1 = df[filtro]


# %%
df.shape
# %%
filtro_1.shape
# %%

filtro_50_100 = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)

filtro_50_100

# %%

#filtro_2 = valores maiores ou iguais a 50 e menores que 100
filtro_2 = df[filtro_50_100]
filtro_2


# %%

filtro_2.shape

# %%

filtro_1.shape

# %%

filtro_1_50 = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)

filtro_1_50

# %%

#filtro_3 = valores iguais a 1 ou iguais a 100
filtro_3 = df[filtro_1_50]
filtro_3

# %%

filtro_3.shape

# %%
