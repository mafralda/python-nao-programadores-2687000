# Crie uma lista apenas com elementos numéricos
salarios = [5000, 2000, 6000, 1800, 9800, 3555, 12000]
salarios

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
minha_lista = [
    42,                        # Inteiro
    3.14,                      # Float
    "Olá, mundo!",             # String
    True,                      # Booleano
    None,                      # NoneType
    [1, 2, 3],                 # Lista (de inteiros)
    (4, 5, 6),                 # Tupla
    {"chave": "valor"},        # Dicionário
    {7, 8, 9},                 # Conjunto
]

print(minha_lista)

# Imprima na tela apenas os 5 primeiros elementos da lista
minha_lista[0:5]

# Crie um slice na lista para que imprima na tela os elementos de índice par
elementos_pares = minha_lista[::2]
print(elementos_pares)

# Remova da lista o último item
minha_lista.pop()
print(minha_lista)

# Insira na lista um novo item
minha_lista.append("Novo item")
print(minha_lista)

# Remova da lista um item específico
minha_lista.remove("Olá, mundo!")
print(minha_lista)
