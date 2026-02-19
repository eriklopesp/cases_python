def combos(n):
    resultado = []

    def backtrack(restante, inicio, caminho):
        if restante == 0:
            resultado.append(caminho)
            return
        
        for i in range(inicio, restante + 1):
            backtrack(restante - i, i, caminho + [i])

    backtrack(n, 1, [])
    
    return resultado

print(combos(10))