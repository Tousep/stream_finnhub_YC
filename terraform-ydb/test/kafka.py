from confluent_kafka import Consumer, Producer
import time
import os

def error_callback(err):
    print('Something went wrong: {}'.format(err))

def kafka_check_topic(event, context):
    message = os.environ["uniq_msg"]
    params = {
        'bootstrap.servers': 'rc1b-aj44j15i0enkcn8v.mdb.yandexcloud.net:9091',
        'security.protocol': 'SASL_SSL',
        'ssl.ca.location': './ca-certificates/Yandex/YandexInternalRootCA.crt',
        'sasl.mechanism': 'SCRAM-SHA-512',
        'sasl.username': 'finnhub',
        'sasl.password': 'finnhub',
        'error_cb': error_callback,
        'group.id': 'test-consumer1',
    }

    p = Producer(params)
    p.produce('finnhub_market', message)
    p.flush(10)

    params = {
        'bootstrap.servers': 'rc1b-aj44j15i0enkcn8v.mdb.yandexcloud.net:9091',
        'security.protocol': 'SASL_SSL',
        'ssl.ca.location': './ca-certificates/Yandex/YandexInternalRootCA.crt',
        'sasl.mechanism': 'SCRAM-SHA-512',
        'sasl.username': 'finnhub_c',
        'sasl.password': 'finnhub_c',
        'error_cb': error_callback,
        'group.id': 'test-consumer1',
        'auto.offset.reset': 'latest',
    }
    c = Consumer(params)
    c.subscribe(['finnhub_market'])

    msg = c.poll(timeout=3.0)
    if msg and msg.value().decode() == message:
        print(msg.value().decode())
        return True
    return False

if __name__ == '__main__':
    kafka_check_topic(1,2)