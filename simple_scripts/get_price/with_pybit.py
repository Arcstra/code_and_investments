from pybit.unified_trading import WebSocket

def handle_message(message):
    # Выводим текущую цену Биткоина
    print(message["data"][0]["close"])

ws = WebSocket(
    testnet=False,  # Для mainnet используйте False
    channel_type="spot"  # linear, inverse, spot
)

# Подписка на свечи (kline)
ws.kline_stream("15", "BTCUSDT", handle_message)

# Для поддержания соединения
try:
    while True:
        True
except KeyboardInterrupt:  # Ctrl+C
    print("STOP!!!")
    ws.exit()  # Закрываем соединение с биржой
