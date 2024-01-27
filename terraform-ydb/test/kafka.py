from kafka import KafkaConsumer


def kafka_check_topic(event, context):
    producer = KafkaProducer(
    bootstrap_servers=['rc1b-namn6f7m2172e4n9.mdb.yandexcloud.net:9091'],
    security_protocol="SASL_SSL",
    sasl_mechanism="SCRAM-SHA-512",
    sasl_plain_username='finnhub',
    sasl_plain_password='finnhub',
    ssl_cafile="./ca-certificates/Yandex/YandexInternalRootCA.crt")

    producer.send('finnhub_market', b'test message', b'key')
    producer.flush()
    producer.close()
    
    consumer = KafkaConsumer(
        'finnhub_market',
        bootstrap_servers=['rc1b-namn6f7m2172e4n9.mdb.yandexcloud.net:9091'],
        security_protocol="SASL_SSL",
        sasl_mechanism="SCRAM-SHA-512",
        sasl_plain_username='finnhub_c',
        sasl_plain_password='finnhub_c',
        ssl_cafile="./ca-certificates/Yandex/YandexInternalRootCA.crt")

    print("ready")

    for msg in consumer:
        if msg.value.decode("utf-8") == 'some payload1':
            return True
    return False

