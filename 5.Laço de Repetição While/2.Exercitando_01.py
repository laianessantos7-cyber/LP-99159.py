import os
os.system("cls")



print("Laço de Repetição- While.")


while True:
    nota=int(input("Digite uma nota: "))
    if nota >=0 and nota<=10:
        break
print(f"Nota: {nota}")
print('FIM')
