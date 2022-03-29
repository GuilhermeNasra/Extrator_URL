# Importando Expressões Regulares
import re

endereco = "Rua Sacopã 150, apartamento 805, Lagoa, Rio de Janeiro, RJ, 22471-180"

# Criando o padrão através do método compile
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

# Fazendo a procura do padrão através do método search e usando o endereço como argumento
busca = padrao.search(endereco)
if busca:
    # Utilizamos o método group() para retornar apenas o padrão encontrado no endereço
    cep = busca.group()
    print(cep)
else:
    pass
