# %%

import pandas as pd

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%

x = clientes.dropna()

# %%
