from confluent_kafka import Consumer, Producer

def error_callback(err):
    print('Something went wrong: {}'.format(err))

def kafka_check_topic(event, context):
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
    p.produce('finnhub_market', 'some payload1')
    p.flush(10)

    c = Consumer(params)
    c.subscribe(['finnhub_market'])
    while True:
        msg = c.poll(timeout=3.0)
        if msg.value().decode() == 'some payload1':
            print(msg.value().decode())
            return True
    return False

if __name__ == '__main__':
    kafka_check_topic(1,2)