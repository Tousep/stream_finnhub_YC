resource "yandex_vpc_network" "finnhub_net" {
  name = "finnhub_net"
  folder_id = var.YC_FOLDER_ID
}

resource "yandex_vpc_subnet" "finnhub_subnet" {
  name           = "finnhub_subnet"
  zone           = "ru-central1-b"
  network_id     = yandex_vpc_network.finnhub_net.id
  v4_cidr_blocks = ["10.5.0.0/24"]
}

resource "yandex_vpc_security_group" "finnhub_sec_gr" {
  name       = "finnhub_sec_gr"
  network_id = yandex_vpc_network.finnhub_net.id

  ingress {
    description    = "Kafka"
    port           = 9091
    protocol       = "TCP"
    v4_cidr_blocks = [ "0.0.0.0/0" ]
  }
  
    ingress {
    description    = "HTTPS (secure)"
    port           = 8443
    protocol       = "TCP"
    v4_cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description    = "clickhouse-client (secure)"
    port           = 9440
    protocol       = "TCP"
    v4_cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description    = "Allow all egress cluster traffic"
    protocol       = "TCP"
    v4_cidr_blocks = ["0.0.0.0/0"]
  }
}