from confluent_kafka import Consumer, Producer
import time
import os
import requests
from clickhouse_driver import Client

def clickhouse_connection_check(event, context):
    response = requests.get(
        'https://{0}:8443'.format(event['FQDN']),
        params={
            'query': 'SELECT version()',
        },
        headers={
            'X-ClickHouse-User': event['ClickHouse-User'],
            'X-ClickHouse-Key': event['ClickHouse-Key'],
        },
        verify='./ca-certificates/Yandex/YandexInternalRootCA.crt'
    )

    response.raise_for_status()
    if response.text:
        print(response.text)
        return True
    return False


if __name__ == '__main__':
    event = {
        'FQDN': 'rc1b-cskcq8u3ogqc385s.mdb.yandexcloud.ne'
        'ClickHouse-User': os.environ["CLICKHOUSE_DB_FINNHUB_USER"]
        'ClickHouse-Key':  os.environ["CLICKHOUSE_DB_FINNHUB_USER_SECRET"]
    }
    assert clickhouse_connection_check(event, 'urec')