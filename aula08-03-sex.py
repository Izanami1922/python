#Fazer um programa que receba o sexo da pessoa, e retorne uma mensagem
sexo = input("Entre com o sexo <M> masculino, <F> feminino e <O> outro:\n")
if (sexo == 'F' or sexo == 'f' or sexo == 'Marcelo'):
    print("Feliz dia das mulheres!")
elif(sexo == 'M' or sexo == 'm'):
    print("Bom dia...")
elif(sexo == 'O' or sexo == 'o'):
    print("Tranformeeer")
else:
    print("Sai fora!")