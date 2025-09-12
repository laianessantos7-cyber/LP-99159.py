import os
os.system("cls")

print("====BOLETIM====")

QUANTIDADE_NOTAS=2
soma=0

for i in range(QUANTIDADE_NOTAS):
    while True:
        n1=int(input(f"Digite a {i+1}º nota: "))
        if n1 >=0 and n1 <=10:
         break

soma= soma+n1
media=(n1+n1)/QUANTIDADE_NOTAS

print(f"Nota: {media}")
print('FIM')