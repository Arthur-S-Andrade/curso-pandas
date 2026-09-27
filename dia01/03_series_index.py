# %%
import pandas as pd

idades =[
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

series_idades = pd.Series(idades)
series_idades

# %%
series_idades = series_idades.sort_values()
series_idades

# %%
print('sem iloc', series_idades[0])
print('com iloc', series_idades.iloc[0])

# %%
print(series_idades.iloc[-1])

# %%
print(series_idades.iloc[:3])

# %%
print(series_idades.iloc[::-1])

# %%

idades =[
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

indexs = ["Téo", "Maria", "Jose", "Luiz", "Ana", "Nah", "Dani", "Mah", "Fer", "Nanda", "Naty", "Nih", "Pedro", "Kozato", "Kozato"]

series_idades = pd.Series(idades, index = indexs)

print(series_idades)

# %%

print(series_idades["Kozato"])
# %%

