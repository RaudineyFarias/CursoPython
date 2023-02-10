import modulo

print ("calculo de IMC")

ent_peso = modulo.peso()
ent_alt = modulo.altura()
imc = modulo.calculo(ent_peso, ent_alt)
conceito = modulo.condicao(imc)
modulo.exibir(conceito)