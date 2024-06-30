def calc_media(nota1,nota2,nota3):
    media = (primeira_nota + segunda_nota + terceira_nota)/3
    return media

def situacao_aluno(media):  
        if media >= 7:
            print("aprovado")
        elif media < 7 and media >= 5:
            media= float(input("Digite a nova média do aluno: "))
            if media >= 7:
                print("aprovado")
            else:
                print("reprovado")  
        else:
            print("reprovado")       


nome = input("Digite o nome do aluno:")
primeira_nota = float(input("Digite a primeira nota do aluno: "))
segunda_nota = float(input("Digite a segunda nota do aluno: "))
terceira_nota = float(input("Digite a terceira nota do aluno: "))
media = calc_media(primeira_nota,segunda_nota,terceira_nota)
situacao_aluno(media)

