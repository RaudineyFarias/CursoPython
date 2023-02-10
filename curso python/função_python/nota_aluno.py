print('Bem vindos ao progarama de notas dos alunos: ')

nome = input('Digite o nome do aluno ou digite 0 para sair: ')

dados_aluno = []

acima_media = []

while nome != '0':
    
    nome2 = dados_aluno.append(nome)

    n1 = float(input('Digite a primeira nota do aluno: '+nome+' : '))
    n2 = float(input('Digite a segunda nota do aluno: '+nome+' : '))
    n3 = float(input('Digite a terceira nota do aluno: '+nome+' : '))

    if n1 >100 or n2>100 or n3>100:
      print('Valor Invalido em algumas das Notas digitadas executa o programa novamente!')
      print('Dados dos alunos inseridos na lista: ',dados_aluno)
      break
    
    dados_aluno.append(n1)
    dados_aluno.append(n2)
    dados_aluno.append(n3)

    media = (n1+n2+n3)/3


    dados_aluno.append("{:.2f}".format(media))


    if media >=80:
        dados_aluno.append("A")
        print('O Aluno: '+nome+' Obteve o Conceito A.')
        print('Segue Notas Obtidas - Nota 1º: ',n1,'| Nota 2º:',n2,'| Nota 3º:',n3)
        print('O Aluno(a) Obteve Média de: '+"{:.2f}".format(media))
        acima_media.append(nome)
        

    elif media >=50 and media <80:
        dados_aluno.append("B") 
        print('O Aluno: '+nome+' Obteve o Conceito B.')
        print('Segue Notas Obtidas - Nota 1º: ',n1,'| Nota 2º:',n2,'| Nota 3º:',n3)
        print('O Aluno(a) Obteve Média de: ',media) 

    else:
        media < 50
        dados_aluno.append('C')
        print('O Aluno: '+nome+' Obteve o Conceito C.')
        print('Segue Notas Obtidas - Nota 1º: ',n1,'| Nota 2º:',n2,'| Nota 3º:',n3)
        print('O Aluno(a) Obteve Média de: ',media)

    dados_aluno.append('|')
    nome = input('Digite o nome do outro aluno ou digite 0 para sair: ')


if nome =='0':
    print('Fim do Programa!')
    print('Dados dos alunos inseridos na lista: ',dados_aluno)
    print(' ')
    print('Alunos que ficaram acima da média: {}'.format(acima_media))
    print('Fim do programa!')