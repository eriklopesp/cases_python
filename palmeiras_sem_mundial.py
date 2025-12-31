print("O Palmeiras, tem mundial?\n")
resposta = input("Sim/Não:\n")

if not resposta.isalpha():
    print("\nResposta inválida. Responda em forma de texto. Mas ainda sim, o Palmeiras não tem mundial!")

elif resposta not in ["Sim", "Não"]:
    print("\nResposta inválida. Por favor, responda com 'Sim' ou 'Não'. Mas ainda sim, o Palmeiras não tem mundial!")

elif resposta == "Sim":
    print("\n51 é pinga! Não adianta, não tem mundial!")

else:
    print("\nEsto es la verdad!, todo mundo sabe.")





