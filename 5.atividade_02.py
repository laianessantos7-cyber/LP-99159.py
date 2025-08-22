#Limpar terminal.
import os
os.system("cls")


n1= int(input("Digite o primeiro número: " ))
print("")
n2= int(input("Digite o segundo número: " ))

soma= n1+n2
print("")
produto=n1*n2
print("")


if soma>produto:
    print(" A soma é menor que o produto")
    maior=n1
    menor=n2

else:
    print("A soma é maior que o produto.")
    maior=n1
    menor=n2
 
print(f"Soma: {soma}") 
print(f"Produto: {produto}")  
print(f"Maior: {maior}")
print(f"Menor: {menor}")



