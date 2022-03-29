import re

# https://bytebank.com.br/cambio
url = 'https://bytebank.com.br/cambio'

padrao_url = re.compile('(http(s)?://)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError('A URL é inválida.')
else:
    print('A URL é válida.')
