
def converter_comprimento(quantidade, medida_entrada, medida_saida):
    medidas = {
        "cm": 1,
        "m": 100,
        "km": 100000,
        "pe": 30.48,
        "polegadas": 2.54,
        "jarda": 91.44,
        "milha": 160934
    }
    
    if medida_entrada != medida_saida:
        if medida_entrada in medidas and medida_saida in medidas:
            return quantidade * medidas[medida_entrada] / medidas[medida_saida]
        else:
            return "Unidade de medida inválida."
    else:
        return "Você não pode converter para a mesma medida."

quantidade = float(input("Digite a quantidade: "))
medida_entrada = input("Digite a medida ATUAL qual a quantidade se refere pode ser: (cm, m, km, pe, polegadas, jarda, milha.): ")
medida_saida = input("Digite a medida para qual deseja Converter : (cm, m, km, pe, polegadas, jarda, milha.): ")
medida_entrada, medida_saida = medida_entrada.lower(), medida_saida.lower()

print(converter_comprimento(quantidade, medida_entrada, medida_saida))