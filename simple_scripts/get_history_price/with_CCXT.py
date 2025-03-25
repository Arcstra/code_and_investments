import datetime
import ccxt

binance = ccxt.binance()  # Выбираем биржу Binance

# Получаем значения свечей
data_btc = binance.fetch_ohlcv(
    symbol="BTC/USDT",  # Биткоина к доллару
    timeframe="4h",  # Продолжительность каждой свечи равна 4 часам
    since=int(datetime.datetime(2025, 3, 1).timestamp()) * 1000,  # С начала марта
    limit=42)  # За неделю (24 / 4 * 7 = 42)

for candle in data_btc:
    # Вычисление изменения цены (в процентах)
    change = (candle[4] - candle[1]) / candle[1] * 100
    # Вычисление даты открытия свечи
    date_now = datetime.datetime.fromtimestamp(candle[0] // 1000)
    # Красивый вывод даты и значения
    print(f"{date_now.strftime('%d.%m.%Y %H:%M')} \t {change: .2f} %")
