import config, csv
from binance.client import Client


client = Client(config.API_KEY, config.API_SECRET)

prices = client.get_all_tickers()

for price in prices:
       print(price)


csvfile = open('2021_15minutes.csv', 'w', newline='') 
candlestick_writer = csv.writer(csvfile, delimiter=',')

# jassy to change to live data
#the kline interval should be configurable (1 min, 5 min,15 min, 30 min)
#(BTCUSDT, nanoudt, adausdt)
candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2021", "22 Jun, 2021")

for candlestick in  candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close()