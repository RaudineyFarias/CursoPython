print("Média do aluno")

qtde_aluno = int(input("Qual a quantidade de alunos? "))

  
if qtde_aluno <=0:
    
    print("Opção Invalida!")
    opcao = input("Deseja continuar? [1} sim [2} não: ") 
  
    if opcao == "2":
        print("Fim do programa!")
    elif opcao =="1":
        qtde_aluno = int(input("Digite a quantidade de alunos? "))
        if qtde_aluno !=0:   
      
            cod_aluno = 0
        
            while cod_aluno <= qtde_aluno:
            
                cod_aluno = cod_aluno+1
        
                mensagem_input = "Qual o nome do aluno [ " + str(cod_aluno) + "] : " 
        
                nome = input( mensagem_input )
        
                n1 = float(input("Qual a primeira nota do aluno "+nome+"? "))
        
                n2 = float(input("Qual a segunda nota do aluno "+nome+"? "))
        
                media = (n1+n2)/2
        
                print("  ")
            
                print("O aluno "+nome+" Obteve a média de "+"{:.2f}".format (media))
                
                print("  ")   