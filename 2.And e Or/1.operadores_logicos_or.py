#Limpar terminal.
import os
os.system("cls")

nota=12

#Se nota menor que zero ou maior que 10.

if nota < 0 or nota > 10:
    print("Nota inválida.")

else:
    print(f"Nota: {nota}")

