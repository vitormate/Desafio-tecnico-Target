def calcula_porcentagem(valor, total):
    return (valor / total) * 100

dados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(dados.values())

for x in dados:
    porcentagem = calcula_porcentagem(dados[x], total)
    print(f"-> {x} representa {porcentagem:.1f}% do faturamento total mensal")
