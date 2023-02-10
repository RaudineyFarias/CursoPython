import numpy
print('Temperatura média de cada mês do ano')


c = 0

t = 0

menor = 0

igual = 0

lista_temp =[]

temp_maior = []

temper_media = []

for i in range(12):
    c = c+1
    mensagem = 'Qual a temperatura do mês de 0'+str(c)+' : '
    temp_mes = float(input(mensagem))
    lista_temp.append(temp_mes)
    if temp_mes > 27.5:
        t = t+1
        if c == 1:
            temp_maior.append('Janeiro')
        elif c == 2:           
            temp_maior.append('Fevereiro')   
        elif c == 3:
            temp_maior.append('Março')    
        elif c == 4:
            temp_maior.append('abril')  
        elif c == 5: 
            temp_maior.append('Maio')    
        elif c == 6:
            temp_maior.append('Junho')   
        elif c == 7:
            temp_maior.append('Julho') 
        elif c == 8:
            temp_maior.append('Agosto') 
        elif c == 9:
            temp_maior.append('Setembro') 
        elif c == 10:
            temp_maior.append('Outubro') 
        elif c == 11:
            temp_maior.append('Novembro') 
        else: 
            c == 12
            temp_maior.append('Dezembro') 

    if temp_mes < 27.5:
        menor = menor+1
    if temp_mes == 27.5:
        igual = igual+1    
        temper_media.append(temp_mes)


media = numpy.mean(lista_temp)

print(' ')
print('Segue na ordem todas as temperaturas informadas: {}'.format(lista_temp))
print('A Temperatura média anual: {:.2f}'.format(media))
print('Quantidade de temperaturas mensais superiores a temperatura média anual: {}'.format(t))
print('Meses com temperaturas superiores a temperatura média anual: {}'.format(temp_maior))
print('Quantidade de temperaturas mensais inferiores a temperatura média anual: {}'.format(menor))
print('Quantidade de temperaturas mensais iguais a temperatura média anual: {}'.format(igual))
print(' ')