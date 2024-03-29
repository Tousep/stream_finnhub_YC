from confluent_kafka import Consumer, Producer
import time
import os

def error_callback(err):
    print('Something went wrong: {}'.format(err))

def kafka_check_topic(event, context):
    message = os.environ["uniq_msg"]
    params = {
        'bootstrap.servers': event['bootstrapServers'],
        'security.protocol': 'SASL_SSL',
        'ssl.ca.location': './ca-certificates/Yandex/YandexInternalRootCA.crt',
        'sasl.mechanism': 'SCRAM-SHA-512',
        'sasl.username': event['user_p'],
        'sasl.password': event['user_p_secret'],
        'error_cb': error_callback,
    }
    p = Producer(params)
    p.produce(event['topic'], event['message'])
    p.flush(10)

    params = {
        'bootstrap.servers': event['bootstrapServers'],
        'security.protocol': 'SASL_SSL',
        'ssl.ca.location': './ca-certificates/Yandex/YandexInternalRootCA.crt',
        'sasl.mechanism': 'SCRAM-SHA-512',
        'sasl.username': event['user_c'],
        'sasl.password': event['user_c_secret'],
        'error_cb': error_callback,
        'group.id': 'test-consumer1',
        'auto.offset.reset': 'latest',
    }

    c = Consumer(params)
    print(1)
    c.subscribe([event['topic']])
    print(2)
    msg = c.poll(timeout=3.0)
    if msg and msg.value().decode() == event['message']:
        print(msg.value().decode())
        return True
    return False

if __name__ == '__main__':
    event = {
        'bootstrapServers': 'rc1b-hdlnk60rkhbd5b1g.mdb.yandexcloud.net:9091',
        'topic': os.environ["KAFKA_FINNHUB_TOPIC"],
        'user_p': os.environ["KAFKA_USER_PRODUCER"],
        'user_p_secret': os.environ["KAFKA_USER_SECRET_PRODUCER"],
        'user_c': os.environ["KAFKA_USER_CONSUMER"],
        'user_c_secret': os.environ["KAFKA_USER_SECRET_CONSUMER"],
        'message': os.environ["uniq_msg"]
    }
    assert kafka_check_topic(event, 'userg')