# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")

clientes.head()

# %%

clientes["qtdePontos"].sort_values()

# %%

clientes.sort_values(by="qtdePontos")

# %%

clientes.sort_values(by="qtdePontos", ascending=False)

# %%

clientes.sort_values(by="qtdePontos", ascending=False).head()

# %%

top_5 = (clientes.sort_values(by="qtdePontos", ascending=False)
                 .head())

top_5["idCliente"]
# %%


brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario": [2345, 4533, 3245, 4533]
    }
)

brinquedo
# %%

brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])

# %%
