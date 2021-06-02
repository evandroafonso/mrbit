from requests import Session  # biblioteca que permite a utilização de API.
import json  # biblioteca JSON permite a manipulação dos dados da API.

# url do site coinmarketcap.com.
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# apresentação de parâmetros para leitura de dados de Bitcoin.
parameters1 = {
    'symbol': 'BTC'
}

# apresentação de parâmetros para leitura de dados do Ethereum.
parameters2 = {
    'symbol': 'ETH'
}

# apresentação de parâmetros para leitura de dados de Litecoin.
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
def apresentacao():
    print('===============================================')
    print('MRBIT - CÂMBIO DE CRIPTOMOEDAS')
    print('compra e venda de Bitcoin, Ethereum e Litecoin.')
    print('===============================================')
    print()
    print('Acompanhe a cotação em tempo real!')
    print('Atualizações a cada 100 segundos')
    print()

# função organiza os dados referente ao Bitcoin
def bitcoin():
    response = session.get(url, params=parameters1)
    parseData = json.dumps(response.json())
    btcObj = json.loads(parseData)
    btcString = float(btcObj['data']['BTC']['quote']['USD']['price'])
    # formatação e apresentação dos dados retirados da API
    print('BTCUSD {0:.2f}'.format(btcString))

# função organiza os dados referente ao Ethereum
def ethereum():
    response = session.get(url, params=parameters2)
    parseData = json.dumps(response.json())
    ethObj = json.loads(parseData)
    ethString = float(ethObj['data']['ETH']['quote']['USD']['price'])
    # formatação e apresentação dos dados retirados da API
    print('ETHUSD {0:.2f}'.format(ethString))

# função organiza os dados referente ao Litecoin
def litecoin():
    response = session.get(url, params=parameters3)
    parseData = json.dumps(response.json())
    ltcObj = json.loads(parseData)
    ltcString = float(ltcObj['data']['LTC']['quote']['USD']['price'])
    # formatação e apresentação dos dados retirados da API
    print('LTCUSD {0:.2f}'.format(ltcString))








