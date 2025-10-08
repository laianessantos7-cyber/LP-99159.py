import os
import time

os.system('cls')

#Criando uma função
def saudacao():
    print('Boa Tarde!')
    time.sleep(3) #Espera 3 segundos.
    os.system('cls')

#Código principal: 
saudacao() # Chamando função.
print('Exemplo de uso de uma função sem parâmetros.')
