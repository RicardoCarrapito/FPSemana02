# Solicita a frase do usuário
frase = input()

# Inicializa o dicionário para contar as ocorrências das letras
contador = {}

# Itera pela frase
for letra in frase:
    # Apenas considera letras (ignorando espaços e caracteres especiais)
    if letra.isalpha():
        # Adiciona ou incrementa a contagem no dicionário
        if letra not in contador:
            contador[letra] = 1
        else:
            contador[letra] += 1

# Exibe o dicionário
print(contador)

