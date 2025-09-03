#Atividade 09- 27/08/2025


#Limpar terminal.
import os
os.system("cls")

quant_maca=int(input("Digite a quantidade de maças desejadas: ") )

if quant_maca < 12:
    print(f" Você comprou {quant_maca} maças:")
    valor_total= quant_maca * 1.30
else:
    print(f"Você comprou {quant_maca} maças: ")
    valor_total= quant_maca * 1.00

print(f" \n O valor total de sua compra é: R$ {valor_total}")




