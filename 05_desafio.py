texto = input("Informe uma string para ser invertida: ")

# Apenas para python
novo_texto = texto[::-1]
print(novo_texto)

# Solução mais geral
def inverter_string(texto):
    nova_string = ""
    i = len(texto) - 1
    while i >= 0:
        nova_string += texto[i]
        i -= 1
    
    return nova_string

nova_string = inverter_string(texto)
print(nova_string)