# Stream processing of Finhub data in YandexCloud

This project is a real-time stream based on Finnhub.io API/websocket transaction data. It demonstrates the key aspects of streaming pipeline design and architecture for low latency, scalability, and availability.

# Architecture
![Arch](https://github.com/Tousep/stram-finnhub2click_ydb/assets/88712939/36468252-9a09-46ac-8e34-6f16cadd0575)
The diagram above gives an idea of ​​the architectural design.

All applications are located in YandexCloud (YC) services. The infrastructure is managed by Terraform.

## Data ingestion layer

Python container application - FinnhubProducer connects to Finnhub.io using webSocket. It splits the messages into atomic records and puts the messages in the finnhub_market topic of the Kafka broker. The Docker is hosted in the Container Registry and fired with a trigger on the Servless Container.

## Message broker layer

Messages from FinnhubProducer are sent to the finnhub_market topic of the Kafka broker, which resides in the Managed Service for Kafka cluster.

## Stream processing layer

The data transfer connects to Kafka using the source endpoint, and connects to the ClickHouse cluster using the destination endpoint and transfers data in real time.

## Serving database layer

The ClickHouse database stores the data received from the transfer. Clichouse is deployed in a Managed Service for ClickHouse cluster.

## Dashboard

Dashboards are built in the DataLens service. Retrieves data from ClickHouse. The dashboard is updated every 30s.
![finnhub_dash](https://github.com/Tousep/stram-finnhub2click_ydb/assets/88712939/2b8cb3cc-6915-4d49-86cb-3ef26b54d615)

# Setup & deployment
       
- Build a container and place it in the Container registry
  docker build . -t cr.yandex/crpklr23obfr3io36pqr/finnhub_producer:a46
  docker push cr.yandex/crpklr23obfr3io36pqr/finnhub_producer:a46
- Create a trigger for regular launch of the container.
- Create a kafka source endpoint for the transfer date.
- Using Terraform to deploy the architecture. by changing the parameters in advance:
   * yandex_datatransfer_transfer
     * source_id - specify the endpoint id from step 3.
   * yandex_serverless_container
     * service_account_id - YC service account ID.
     * KAFKA_SERVER is the address of the Kafka cluster.
     * FINNHUB_API_TOKEN - API key for connecting to finnhub webSocket (need to register).
     * url - url of the container loaded in step 1.
   * yandex provider
     * service_account_key_file - File with keys for connecting to the cloud
     * folder_id - YC resource manager directory address
   * yandex_container_registry
     * folder_id - YC resource manager directory address
  
# Potential improvements
* Creation of a single configuration file for deployment options.
* Using Yandex Secrets for keys.
* Add a deployment trigger to launch a data ingestion layer container in terraform scripts.
* Add Kafka source endpoint deployment in terraform scripts.
* Code cleanup  and further development



# Ru-docs
# Потоковая обработка данных Finhub в YandexCloud

Данный проект представляет собой поток реального времени на основе данных транзакций Finnhub.io API/websocket. Он демонстрирует ключевые аспекты проектированияи архитектуры стримминг конвейера для обеспечения низкой задержки, масштабируемости и доступности.

# Архитектура
![Arch](https://github.com/Tousep/stram-finnhub2click_ydb/assets/88712939/36468252-9a09-46ac-8e34-6f16cadd0575)
Диаграмма выше дает представление об архитектуре проекта.

Все приложения распологаются в сервисах YandexCloud (YC). Инфраструктурой управляет Terraform.

## Уровень приема данных

Контейнерное приложение Python - FinnhubProducer подключается к веб-сокету Finnhub.io. Он разбивает сообщения на атомарные записи и помещает сообщения в топик finnhub_market брокера Kafka. Котнейнер размещен в Container Registry и запускается с помощью триггера в Servless Container.

## Уровень брокера сообщений 

Сообщения от FinnhubProducer передаются в топик finnhub_market брокера Kafka , который расположен в кластере Managed Service for Kafka.

## Уровень потоковой обработки 

Трансфер данных с помощью эндпоинта источника подключается к Kafka, а с помощью эндпоинта назначения подключается к кластеру ClicHouse и в режиме реального времени переносит данные.

## Уровень базы данных

База данных ClickHouse хранит данные полученные из трансфера. Clichouse развернут в клвстере Managed Service for ClickHouse.

## Уровень визуализации

Дашборды построенны в сервисе DataLens. Извлекает данные из ClickHouse. Панель мониторинга обновляется каждые 30с.
![finnhub_dash](https://github.com/Tousep/stram-finnhub2click_ydb/assets/88712939/2b8cb3cc-6915-4d49-86cb-3ef26b54d615)

# Настройка и развертывание

- собрать контейнер и поместить его в Container registry
  docker build . -t cr.yandex/crpklr23obfr3io36pqr/finnhub_producer:a46
  docker push cr.yandex/crpklr23obfr3io36pqr/finnhub_producer:a46
- создать триггер на регулярный запуск контейнера.
- Создать эндпоинт источника kafka для дата трансфера.
- Развернуть архитектуру с помоью Terraform развернуть архитектуру. предварительно изменив параметры:
   * yandex_datatransfer_transfer
     * source_id - указать id эндпоинта из шага 3.
   * yandex_serverless_container
     * service_account_id - идентификатор сервисного аккауна YC.
     * KAFKA_SERVER - адрес кластера Kafka.
     * FINNHUB_API_TOKEN - Ключ API для подключения к webSocket finnhub(нужно зарегистрироваться).
     * url - url загруженного в шаге 1 контейнера.
   * provider yandex
     * service_account_key_file - Файл с ключами для подключения к облаку
     *  folder_id - адрес каталога ресурс менеджера YC
   * yandex_container_registry
     *  folder_id - адрес каталога ресурс менеджера YC
  
# Потенциальные улучшения
* Создание единного конфигурационного файла для параметров развертывания.
* Использование Yandex Secrets для ключей.
* Добавленеи развертываня триггера запуск контейнера уровня приема данных с использованием terraform.
* Добавленеи развертываня эндпоинта источника Kafka с использованием terraform.
* Рефакторинг кода и дальнейшее развитие
