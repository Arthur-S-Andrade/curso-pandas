# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes

# %%

filtro = clientes["qtdePontos"] == 0
filtro

# %%

clientes_0 = clientes[filtro]
clientes_0["flag_1"] = 1
clientes_0

# %%
