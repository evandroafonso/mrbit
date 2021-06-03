from requests import Session  # biblioteca que permite a utilização de API.
import json  # biblioteca JSON permite a manipulação dos dados da API.

# url do site coinmarketcap.com.
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# dicionário reúne os parâmetros para leitura de dados de Bitcoin.
parameters1 = {
    'symbol': 'BTC'
}

#  dicionário reúne os parâmetros para leitura de dados do Ethereum.
parameters2 = {
    'symbol': 'ETH'
}

# dicionário reúne os parâmetros para leitura de dados de Litecoin.
parameters3 = {
    'symbol': 'LTC'
}

headers = {
    'Accepts': 'application/json',
    # chave de acesso da API com o programa.
    'X-CMC_PRO_API_KEY': '8b7dea6f-bdd0-4be2-ac2e-01ad7770cbc0',
}

session = Session()
session.headers.update(headers)


# função de apresentação do programa
def presentation():
    print('===============================================')
    print('       MRBIT - CÂMBIO DE CRIPTOMOEDAS          ')
    print('compra e venda de Bitcoin, Ethereum e Litecoin.')
    print('===============================================')
    print()
    print('Acompanhe a cotação em tempo real!')
    print('Atualizações a cada 100 segundos')
    print()


# função organiza/formata os dados referente ao Bitcoin
def bitcoin():
    response = session.get(url, params=parameters1)
    parse_data = json.dumps(response.json())
    btc_obj = json.loads(parse_data)
    btc_num = float(btc_obj['data']['BTC']['quote']['USD']['price'])
    # formatação e apresentação dos dados retirados da API
    print('BTCUSD {0:.2f}'.format(btc_num))


# função organiza/formata os dados referente ao Ethereum
def ethereum():
    response = session.get(url, params=parameters2)
    parse_data = json.dumps(response.json())
    eth_obj = json.loads(parse_data)
    eth_num = float(eth_obj['data']['ETH']['quote']['USD']['price'])
    # formatação e apresentação dos dados retirados da API
    print('ETHUSD {0:.2f}'.format(eth_num))


# função organiza/formata os dados referente ao Litecoin
def litecoin():
    response = session.get(url, params=parameters3)
    parse_data = json.dumps(response.json())
    ltc_obj = json.loads(parse_data)
    ltc_num = float(ltc_obj['data']['LTC']['quote']['USD']['price'])
    # formatação e apresentação dos dados retirados da API
    print('LTCUSD {0:.2f}'.format(ltc_num))
