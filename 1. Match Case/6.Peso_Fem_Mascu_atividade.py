#Atividade 6- 03/09/2025


#Limpar terminal.
import os
os.system("cls")


altura=float(input("Digite sua altura: "))
genero=input("Digite seu genêro: ")

 
match genero:
    case 'M':
         genero = (72.7 * altura ) - 58
         print (f"Masculino:{genero: .2f}")
    case 'F':
         genero = (62.1 * altura )- 44.7
         print(f"Feminino:{genero: .2f}")
    
    case _: "Inválido."
     