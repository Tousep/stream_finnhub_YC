from confluent_kafka import Consumer, Producer
import time
import os
import requests
from clickhouse_driver import Client

def clickhouse_connection_check(event, context):

    # client = Client(host='rc1b-cskcq8u3ogqc385s.mdb.yandexcloud.net',
    #                 user='finnhub_cl',
    #                 password='finnhub_cl',
    #                 port=9000,
    #                 secure=True,
    #                 verify=True,
    #                 ca_certs='./ca-certificates/Yandex/RootCA.crt')

    # print(client.execute('SELECT version()'))
    response = requests.get(
        'https://{0}:8443'.format('rc1b-cskcq8u3ogqc385s.mdb.yandexcloud.net'),
        params={
            'query': 'SELECT version()',
        },
        headers={
            'X-ClickHouse-User': 'finnhub_cl',
            'X-ClickHouse-Key': 'finnhub_cl',
        },
        verify='./ca-certificates/Yandex/YandexInternalRootCA.crt'
    )

    response.raise_for_status()
    print(response.text)


if __name__ == '__main__':
    assert clickhouse_connection_check(1,2)