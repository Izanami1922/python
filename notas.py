#Digite 10 notas de alunos e retorne a media das notas

cont = 0
n = 0

while(cont < 10):
    n += float(input("Digite a nota do aluno:"))
    cont+=1  
print(f"A média das notas é: {(n/10):.2f}")
