quantidade = int(input('Digite a quantidade de alunos: '))


for notas in range(quantidade):
    alunos = input('Digite o nome do aluno:')
    notas1 = int(input('Digite a nota do aluno:'))
    notas2 = int(input('Digite a nota do aluno:'))
    notas3 = int(input('Digite a nota do aluno:'))
    soma = notas1 + notas2 + notas3
    media = soma / 3
    print(media)
    
    if media > 6:
        print(f'{alunos} foi aprovado')
    elif media < 6:
        print(f'{alunos} reprovado')
    

    

