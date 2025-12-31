import time
import pandas as pd

inicio = time.time()
twitch = pd.read_csv(r"C:\Users\Eriklopesp\Downloads\Sessão de transmissão de 09_07_2025 a 09_07_2025.csv")

print(twitch)

twitch.to_csv(r"C:\Users\Eriklopesp\Downloads\Sessão_de_transmissão_de_09_07_2025_a_09_07_2025.csv", index=False)

fim = time.time()
duracao = fim - inicio
print(f"Tempo de execução: {duracao:.2f} segundos")