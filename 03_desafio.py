from dados import dados

dados_reais = []
total = 0

for x in dados:
    if x["valor"] != 0:
        dados_reais.append(x)
        total += x["valor"]

menor = dados_reais[0]
maior = dados_reais[0]
media = total / len(dados_reais)
dias_superior = 0

for i in range(1, len(dados_reais)):
    if dados_reais[i]["valor"] < menor["valor"]:
        menor = dados_reais[i]
    if dados_reais[i]["valor"] > maior["valor"]:
        maior = dados_reais[i]
    if dados_reais[i]["valor"] > media:
        dias_superior += 1

print(f"O menor valor de faturamento ocorreu no dia {menor["dia"]}. FATURAMENTO: R${menor["valor"]}")
print(f"O maior valor de faturamento ocorreu no dia {maior["dia"]}. FATURAMENTO: R${maior["valor"]}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {dias_superior} dias")