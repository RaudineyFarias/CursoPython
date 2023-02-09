print ("calculo de IMC")

peso = float( input("Qual o seu peso? "))

altura = float( input("Qual a sua altura? "))

imc = (peso/(altura*altura))

if (imc <18.5):
  print("O seu IMC é: "+"{:.0f}".format (imc))
  print("Você está abaixo do seu peso ideal")
  
elif (imc >=18.5 and imc<=24.9):
  print("O seu IMC é: "+"{:.0f}".format (imc))
  print("Parabéns! Você está no seu peso ideal!")
  
elif (imc >=25.0 and imc<=29.9): 
  print("O seu IMC é: "+"{:.0f}".format (imc))
  print("Você está acima do seu peso (sobrepeso)")
  
elif (imc >=30.0 and imc  <=34.9):
  print("O seu IMC é: "+"{:.0f}".format (imc))
  print("Obesidade grau I")
  
elif (imc >=35.0 and imc <=39.9):
  print("O seu IMC é: "+"{:.0f}".format (imc))
  print("Obesidade grau II")

else:
  print("O seu IMC é: "+"{:.0f}".format (imc))
  print("Obsesidade grau III")