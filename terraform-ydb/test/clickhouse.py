from confluent_kafka import Consumer, Producer
import time
import os
import requests
from clickhouse_driver import Client

def clickhouse_connection_check(event, context):

    client = Client(host='<FQDN_любого_хоста_ClickHouse®>',
                    user='<имя_пользователя_БД>',
                    password='<пароль_пользователя_БД>',
                    port=9000,
                    secure=True,
                    verify=True,
                    ca_certs='./ca-certificates/Yandex/RootCA.crt')

    print(client.execute('SELECT version()'))
    # response = requests.get(
    #     'https://{0}:8443'.format('rc1b-063qep40gn13ubgg.mdb.yandexcloud.net'),
    #     params={
    #         'query': 'SELECT version()',
    #     },
    #     headers={
    #         'X-ClickHouse-User': 'finnhub_cl',
    #         'X-ClickHouse-Key': 'finnhub_cl',
    #     },
    #     verify='./ca-certificates/Yandex/YandexInternalRootCA.crt'
    # )

    # response.raise_for_status()
    # print(response.text)


if __name__ == '__main__':
    clickhouse_connection_check(1,2)