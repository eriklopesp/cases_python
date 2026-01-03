import pandas as pd
from sklearn.linear_model import LinearRegression

dados = {
    "mes": [1, 2, 3, 4, 5],
    "gastos": [100, 120, 130, 150, 170]
}

df = pd.DataFrame(dados)

# entrada (X) e saída (y)
X = df[["mes"]]      # feature
y = df["gastos"]     # target

# cria o modelo
modelo = LinearRegression()

# treinamento
modelo.fit(X, y)

# previsão de um mês futuro
previsao = modelo.predict([[6]])

print(previsao)
