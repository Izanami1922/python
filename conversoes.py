#Elabore um programa que seja capaz de realizar as seguintes conversões: 1-Litro pra mililitro, 2-quilômetro pra metro e 3-toneladas pra gramas
conver = input("Qual conversão você quer realizar?\n 1-Litro para mililítro\n 2-Qilômetro para metro\n 3-Tonelada para gramas\n")
if(conver == '1'):
    l = float(input("Informe quantos litros:\n"))
    mili = (l*1000)
    print("A conversão em mililítros é: ", mili)
elif(conver =='2'):
    q = float(input("Informe quantos quilômetros: \n"))
    print("A conversão em metros é: ", (q*1000))
elif(conver == '3'):
    t = float(input("Informe quantas toneladas: \n"))
    print("A conversão em gramas é: ", (t*1000000))
else:
    print("Larga de ser burro!")