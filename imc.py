p = float(input("Informe seu peso em Kg.: \n"))
a = float(input("Informe sua altura em Metros(ex.: 1.80): \n"))
imc = (p/(a*a))
print(f"Seu IMC é: {imc:.2f}")
if(imc < 17):
    print("Muito abaixo do peso!")
elif(imc < 18.5):
    print("Abaixo do peso")
elif(imc < 25):
    print("Peso normal")
elif(imc < 30):
    print("Acima do peso")
elif(imc < 35):
    print("Obesidade I")
elif(imc < 40):
    print("Obesidade II(severa)")
elif(imc > 40):
    print("Obesidade III(mórbida)")