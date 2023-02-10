import modulo

print("programa de calculo de Notas")

nome = modulo.nome_alu()
capturar_notas = modulo.notas()
media_aluno = modulo.media(capturar_notas)
condicao = modulo.conceito(media_aluno)
modulo.Exibir(nome, media_aluno, condicao, capturar_notas)