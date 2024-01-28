from confluent_kafka import Consumer, Producer
import time
import os
import requests

def clickhouse_connection_check(event, context):

    response = requests.get(
        'https://{0}.mdb.yandexcloud.net:8443'.format('rc1b-063qep40gn13ubgg'),
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
    clickhouse_connection_check(1,2)