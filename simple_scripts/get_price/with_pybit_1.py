from pybit.unified_trading import WebSocket

def handle_message(message):
    # print(message)
    open = float(message["data"][0]["open"])
    close = float(message["data"][0]["close"])
    if not message["data"][0]["confirm"]:
        # Свеча ещё не закрыта, поэтому выводим только цену
        print(f"BTC:\t {close}")
        return
    
    # Свеча закрыта, поэтому можно подвести итоги свечи
    # Например, проверить изменение цены относительно уровня
    if open // 1000 != close // 1000:
        if percent > 0:
            # Цена Биткоина перескочила уровень
            print(f"BTC пробил {close // 1000 * 1000}!")
        else:
            # Цена Биткоина опустилась ниже уровня
            print(f"BTC опустился ниже {close // 1000 * 1000}!")
    percent = (close - open) / open * 100
    # Выводим текущую цену Биткоина + процент изменения цены
    print(f"BTC:\t {close}\t{percent: .2f} %")

ws = WebSocket(
    testnet=False,  # Для mainnet используйте False
    channel_type="spot"  # linear, inverse, spot
)

# Подписка на свечи (kline)
ws.kline_stream("1", "BTCUSDT", handle_message)

# Для поддержания соединения
try:
    while True:
        True
except KeyboardInterrupt:  # Ctrl+C
    print("STOP!!!")
    ws.exit()  # Закрываем соединение с биржой
