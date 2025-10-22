import os
os.system("cls")

def calcular_imc(peso, altura):
    return peso / (altura * altura)


def situacao(imc):
    if imc >= 40:
        classificacao = "Obesidade grau III"
        recomendacao = "Busque assistência médica imediatamente."
    elif imc >= 35:
        classificacao = "Obesidade grau II"
        recomendacao = "Consulte um médico para avaliação e orientação."
    elif imc >= 30:
        classificacao = "Obesidade grau I"
        recomendacao = "Procure orientação de um profissional de saúde."
    elif imc >= 25:
        classificacao = "Sobrepeso"
        recomendacao = "Considere uma dieta balanceada e atividade física."
    elif imc >= 18.5:
        classificacao = "Peso normal"
        recomendacao = "Mantenha hábitos saudáveis."
    else:
        classificacao = "Abaixo do peso"
        recomendacao = "Consulte um nutricionista para orientação."
    return classificacao, recomendacao

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = calcular_imc(peso, altura)
classificacao, recomendacao = situacao(imc)

print("\n= Exibindo resultados=")
print(f"IMC: {imc}")
print(f"Classificação: {classificacao}")
print(f"Recomendação: {recomendacao}")