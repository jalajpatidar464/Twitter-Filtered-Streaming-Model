"""Collecting tweets from get_stream function"""
import logging
import tweepy
import requests
import json
import datetime
import backtrader as bt
from load_configuration import load_configuration_file


class TwitterStrategy(bt.Strategy):

    def __init__(self):
        self.senti = 1

    def next(self):
        if not self.position and self.senti > 0:
            self.buy(size=0.01)
            print("Buy Order Successfully Executed")
            logging.info("Yes executed")
            self.env.runstop()


cerebro = bt.Cerebro()
cerebro.addstrategy(TwitterStrategy)

fromdate = datetime.datetime.strptime('2021-06-15', '%Y-%m-%d')
todate = datetime.datetime.strptime('2021-06-22', '%Y-%m-%d')

data = bt.feeds.GenericCSVData(dataname='2021_15minutes.csv', dtformat=2, compression=15, timeframe=bt.TimeFrame.Minutes, fromdate=fromdate, todate=todate)

cerebro.adddata(data)

file_data = load_configuration_file()

auth = tweepy.OAuthHandler(file_data['cred']["CONSUMER_KEY"], file_data['cred']["CONSUMER_SECRET"])
auth.set_access_token(file_data['cred']["ACCESS_TOKEN"], file_data['cred']["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth)

logging.info('Calling get stream')

def get_stream(headers):
    """Initialise the stream and receive data"""

    while True:
        try:
            with requests.get("https://api.twitter.com/2/tweets/sea"
                              "rch/stream", headers=headers, stream=True) as response:

                logging.info(response.status_code)
                if response.status_code != 200:
                    raise Exception(
                        "Cannot get stream (HTTP {}): {}".format(
                            response.status_code, response.text
                        )
                    )
                try:
                    for response_line in response.iter_lines():
                        if response_line == b'':
                            continue
                        else:
                            json_response = json.loads(response_line)
                            cerebro.run()
                            logging.info('Running Successfully')

                except :
                    logging.warning("5 minute termination msg")

        except:
            logging.error("ConnectionError")