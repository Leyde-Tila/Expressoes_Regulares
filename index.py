def encontrar_select(texto):
    palavra = "SELECT"
    tamanho = len(palavra)

    for i in range(len(texto) - tamanho + 1):
        encontrado = True
        for j in range(tamanho):
            if texto[i + j].lower() != palavra[j].lower():
                encontrado = False
                break
        if encontrado:
            return True
    return False

# Testes
print(encontrar_select("O comando select é muito usado."))  # True
print(encontrar_select("Esse é um exemplo de SEleCt SQL."))  # True
print(encontrar_select("Não há palavra-chave aqui."))  # False
