from limpa_cpf import LimpaCPF

cpf = "123.456.789-00"

cpf = LimpaCPF.fix(cpf=cpf)

print(cpf)
