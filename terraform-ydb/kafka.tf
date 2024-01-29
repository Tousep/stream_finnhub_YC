resource "yandex_mdb_kafka_cluster" "finnhub" {
  environment         = "PRODUCTION"
  name                = "finnhub"
  network_id          = yandex_vpc_network.finnhub_net.id
  subnet_ids          = flatten([yandex_vpc_subnet.finnhub_subnet.id]) ## flatten - костыль, без него ошибка Inappropriate value for attribute "subnet_ids": list of string required.
  security_group_ids  = [ yandex_vpc_security_group.finnhub_sec_gr.id ]
  deletion_protection = false
  config {
    assign_public_ip = true
    brokers_count    = 1
    version          = "3.4"
    kafka {
      resources {
        disk_size          = 10
        disk_type_id       = "network-ssd"
        resource_preset_id = "s2.micro"
      }
      kafka_config {}
    }

    zones = [
      "ru-central1-b"
    ]
  }
  
}
resource "yandex_mdb_kafka_topic" "finnhub_market" {
  cluster_id         = yandex_mdb_kafka_cluster.finnhub.id
  name               = var.KAFKA_FINNHUB_TOPIC
  partitions         = 1
  replication_factor = 1
  topic_config {
    flush_messages   = 2
  }
}

resource "yandex_mdb_kafka_user" "finnhub_market_p" {
  cluster_id = yandex_mdb_kafka_cluster.finnhub.id
  name       = var.KAFKA_USER_PRODUCER
  password   = var.KAFKA_USER_SECRET_PRODUCER
  permission {
    topic_name = var.KAFKA_FINNHUB_TOPIC
    role       = "ACCESS_ROLE_PRODUCER"
  }
}

resource "yandex_mdb_kafka_user" "finnhub_market_c" {
  cluster_id = yandex_mdb_kafka_cluster.finnhub.id
  name       = var.KAFKA_USER_CONSUMER
  password   = var.KAFKA_USER_SECRET_CONSUMER
  permission {
    topic_name = var.KAFKA_FINNHUB_TOPIC
    role       = "ACCESS_ROLE_CONSUMER"
  }
}
