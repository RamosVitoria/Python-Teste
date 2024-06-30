nome = input("Digite o nome do aluno:")
primeira_nota = float(input("Digite a primeira nota do aluno: "))
segunda_nota = float(input("Digite a segunda nota do aluno: "))
terceira_nota = float(input("Digite a terceira nota do aluno: "))
media = (primeira_nota + segunda_nota + terceira_nota)/3

if media >= 7:
   print(nome,"você foi aprovado")
elif media < 7 and media >= 5:
    media= float(input("Digite a nova média do aluno: "))
    if media >= 7:
        print(nome,"você foi aprovado")
    else:
        print(nome,"você foi reprovado")  
else:
    print(nome,"você foi reprovado")               

