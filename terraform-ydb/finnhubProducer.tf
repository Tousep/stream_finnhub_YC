resource "yandex_serverless_container" "finnhubProducer" {
   name               = "finnhub-producer"
   memory             = 256
   service_account_id = var.YC_SERVICE_ACCOUNT_ID
    connectivity {
        network_id = yandex_vpc_network.finnhub_net.id
    }
   concurrency = 1
   image {
      url = "cr.yandex/${var.YC_CONTAINER_REGISTRY}/finnhub_producer:latest"
      environment = {
            FINNHUB_STOCKS_TICKERS=jsonencode(var.finnhub_stocks_tickers)
            FINNHUB_API_TOKEN=var.FINNHUB_API_KEY
            FINNHUB_VALIDATE_TICKERS="1"
            KAFKA_SERVER="rc1b-hdlnk60rkhbd5b1g.mdb.yandexcloud.net"
            KAFKA_PORT="9091"
            KAFKA_SSL_PATH="/usr/local/share/ca-certificates/Yandex/YandexInternalRootCA.crt"
            KAFKA_TOPIC_NAME=var.KAFKA_FINNHUB_TOPIC
            KAFKA_MIN_PARTITIONS="1"
            security_protocol="SASL_SSL",
            sasl_mechanism="SCRAM-SHA-512",
            sasl_plain_username=var.KAFKA_USER_PRODUCER,
            sasl_plain_password=var.KAFKA_USER_SECRET_PRODUCER
      }
    
  }
}
