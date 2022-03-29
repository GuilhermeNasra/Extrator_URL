# Importanto RegEx
import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    @staticmethod
    def sanitiza_url(url):
        if type(url) == str:  # __eq__
            return url.strip()
        else:
            return ""

    # Forma Pythonica de verificar se uma URL está vazia
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia.")
        else:
            pass

        # Enquanto o [] significa um dos caracteres do intervalo, o () significa o valor
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url_0)

        if not match:
            raise ValueError('A URL é inválida.')
        else:
            print('A URL é válida.')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametros(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

    @staticmethod
    def conversao():
        valor_dolar = 4.77
        moeda_origem = extrator_url.get_valor_parametros("moedaOrigem")
        moeda_destino = extrator_url.get_valor_parametros("moedaDestino")
        quantidade = extrator_url.get_valor_parametros("quantidade")

        if moeda_origem == 'real':
            print(f'A conversão de {moeda_origem} para {moeda_destino} é: {float(quantidade) / valor_dolar}')
        else:
            print(f'A conversão de {moeda_origem} para {moeda_destino} é: {float(quantidade) * valor_dolar}')


url_0 = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url_0)
extrator_url_2 = ExtratorURL(url_0)

# DESAFIO DOLAR PARA REAL
print(extrator_url.conversao())

# Estão em endereços de memória diferentes
print(id(extrator_url))
print(id(extrator_url_2))

# Após sobrescrever o print, o extrator_url == extrator_url_2 retornam True
print(extrator_url == extrator_url_2)

print('O tamanho da URL: ', len(extrator_url))
print(extrator_url)

valor_quantidade = extrator_url.get_valor_parametros('quantidade')
print(valor_quantidade)
