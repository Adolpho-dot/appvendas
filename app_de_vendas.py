print("----Bem vindos a loja de Marmitas do Adolpho Evaristo Corrêa Neto----")
print("-------------------------------Cardápio------------------------------")
print("------| Tamanho |  Bife Acebolado(BA)  |  Filé de Frango(FF)  |------")
print("------|    P    |        R$ 16.00      |        R$ 15.00      |------")
print("------|    M    |        R$ 18.00      |        R$ 17.00      |------")
print("------|    G    |        R$ 22.00      |        R$ 21.00      |------")
print("----------------------------------------------------------------------")

total = 0 #Toal usada para somar os valores dos pedidos
#Selecionar sabor e Tamanho
while True:
    while True:
        sabor = input("Entre com o sabor desejado: (BA/FF): ")
        if sabor in ["BA", "FF"]:
            break
        else:
            print("Sabor Invalido. Tente novamente.")

    while True:
        tamanho = input("Entre com o tamanho desejado: (P/M/G): ")
        if tamanho in ["P", "M", "G"]:
            break
        else:
            print("Tamanho Invalido. Tente novamente.")
            
    #Calcular o total a ser pago
    if sabor == "BA":
        if tamanho == "P":
            preco = 16.00
            total += 16.00
        elif tamanho == "M":
             preco = 18.00
             total += 18.00
        else:
             preco = 22.00
             total += 22.00
        print(f"Você pediu um Bife Acebolado no tamanho {tamanho} no valor de R$  {preco:.2f}")
        
    elif sabor == "FF":
        if tamanho == "P":
            preco = 15.00
            total += 15.00
        elif tamanho == "M":
            preco = 17.00
            total += 17.00 
        else:
            preco = 21.00  
            total += 21.00    
             
        print(f"Você pediu um Filé de Frango no tamanho {tamanho} no valor de R$  {preco:.2f}")
        
    continuar = input("Deseja pedir mais alguma coisa? (S/N): ")
    if continuar == "S":
        continue
    else:
        break
   #Mostra o valor total somando os valores dos itens selecionados
print(f"O valor total a ser pago é de R$ {total:.2f}.")