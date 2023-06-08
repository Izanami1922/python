#digite preços de vário produtos e ao final retorne o valor total, flag = 0

p=0
valor=0
flag=1
flag=float(input("Deseja cadastrar um novo produto <1> Sim ou <0> Não \n")) 

while flag != 0:  
    valor=float(input("Informe o valor do produto ou <0> quando terminar:"))  
    p+=valor
    flag=valor
    if(flag == 0):
        print(f"O valor total é: R$ {p:.2f}")
        break
  
    