# url = "bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"

url = ""

# Sanitização da URL (Tratamento da URL, ou seja, retirar os espaços em branco ou
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia.")
else:
    pass

# Separa a base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]

# Fatiamento da string para obter os parâmetros após o ponto de interrogação
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Colocando o parâmetro que estamos buscando
parametro_busca = 'moedaOrigem'

# Encontrar o índice do parâmetro que estamos buscando
indice_parametro = url_parametros.find(parametro_busca)

# Adicionamos ao indice_parametro o método len para obter apenas o valor
indice_valor = indice_parametro + len(parametro_busca) + 1

# Descobrindo o índice do & a partir do indice_valor
# Caso não tenha & após o indice_valor, o find retornará -1
indice_e_comercial = url_parametros.find('&', indice_valor)

# Criando resposta para os dois tipos de casos
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)
