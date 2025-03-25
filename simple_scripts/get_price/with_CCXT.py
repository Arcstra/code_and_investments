import ccxt

binance = ccxt.binance()  # Выбираем биржу Binance

# Получаем данные о торговой паре BTC/USDT в данный момент
data_btc = binance.fetch_ticker("BTC/USDT")

print(data_btc["last"])  # Выводим текущую цену на Bitcoin
