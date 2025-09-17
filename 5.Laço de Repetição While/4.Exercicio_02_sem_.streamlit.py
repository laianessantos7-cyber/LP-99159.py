import os
os.system("cls")

print("====BOLETIM====")

QUANTIDADE_NOTAS=2
soma=0

for i in range(QUANTIDADE_NOTAS):
    while True:
        n1 = float(input(f"Digite a {i+1}ª nota: "))
        if n1 < 0 or n1 > 10:
            print('❌ Nota inválida! Digite novamente.')
        else:
            soma += n1
            break  

media = soma / QUANTIDADE_NOTAS

print(f"\nMédia final: {media:.2f}")