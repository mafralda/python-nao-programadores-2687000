nome = "Sheila"
idade = 46
resumo = f"{nome} é uma mulher de {idade} anos que deseja mudar de profissão, por isso está estudando 'python'."

# Imprima na tela a variável "resumo"
print(resumo)

# Imprima na tela apenas a segunda letra da variável
print(resumo[1])

# Imprima na tela a idade de Paloma (resposta esperada: "46")
print(idade)

# Imprima na tela o trecho final da variável
  # Divide a string em palavras
palavras = resumo.split()
  # Acessa a última palavra
ultima_palavra = palavras[-1]
  # Imprime a última palavra
print(ultima_palavra)

# Converta todos as letras para minúsculo e imprima na tela
print(resumo.lower())

# Converta todas as letras para maiúscula e imprima na tela
print(resumo.upper())

# Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela
print(resumo.title())

# Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela
print(resumo.capitalize())

# Imprima na tela uma string utilizando uma variável, usando o recurso string formato
print(resumo)