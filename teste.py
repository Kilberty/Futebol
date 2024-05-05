valor = "18/40 (45%)"

# Dividindo a string com base no caractere de barra ("/")
antes_barra, resto = valor.split("/")

# Extraindo o número antes da barra
numero_antes_barra = antes_barra.strip()

# Dividindo o restante da string com base no parêntese aberto "("
depois_barra = resto.split("(")[0].strip()

print(numero_antes_barra)    # Saída: "18"
print(depois_barra)
print('Oi')