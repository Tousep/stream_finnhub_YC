#Main file for Finnhub API & Kafka integration
import os
import ast
import json
import websocket
from utils.webSocket2kafka import *

#proper class that ingests upcoming messages from Finnhub websocket into Kafka
class FinnhubProducer:
    
    def __init__(self):
        
        print('Environment:')
        for k, v in os.environ.items():
            print(f'{k}={v}')
        self.finnhub_client = load_client(os.environ['FINNHUB_API_TOKEN'])
        self.producer = load_producer(f"{os.environ['KAFKA_SERVER']}:{os.environ['KAFKA_PORT']}"
                                    , f"{os.environ['security_protocol']}",
                                    f"{os.environ['sasl_mechanism']}",
                                    f"{os.environ['sasl_plain_username']}",
                                    f"{os.environ['sasl_plain_username']}",
                                    f"{os.environ['KAFKA_SSL_PATH']}")
        self.avro_schema = load_avro_schema('/app/src/schemas/trades.avsc')
        self.tickers = ast.literal_eval(os.environ['FINNHUB_STOCKS_TICKERS'])
        self.validate = os.environ['FINNHUB_VALIDATE_TICKERS']
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(f'wss://ws.finnhub.io?token={os.environ["FINNHUB_API_TOKEN"]}',
                              on_message = self.on_message,
                              on_error = self.on_error,
                              on_close = self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def on_message(self, ws, message):
        message = json.loads(message)
        print(message['type'])
        for i in message['data']:
            print(json.dumps(i).encode('utf-8'))
            self.producer.send(os.environ['KAFKA_TOPIC_NAME'], json.dumps(i).encode('utf-8'))
        # avro_message = avro_encode(
        #     {
        #         'data': message['data'],
        #         'type': message['type']
        #     }, 
        #     self.avro_schema
        # )
        # print('..........................................................')
        # print(avro_message)
        # self.producer.send(os.environ['KAFKA_TOPIC_NAME'], avro_message)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")

    def on_open(self, ws):
        type(self.tickers)
        for ticker in self.tickers:
            if self.validate=="1":
                if(ticker_validator(self.finnhub_client,ticker)==True):
                    ws.send(f'{{"type":"subscribe","symbol":"{ticker}"}}')
                    print(f'Subscription for {ticker} succeeded')
                else:
                    print(f'Subscription for {ticker} failed - ticker not found')
            else:
                ws.send(f'{{"type":"subscribe","symbol":"{ticker}"}}')

if __name__ == "__main__":
    FinnhubProducer()
