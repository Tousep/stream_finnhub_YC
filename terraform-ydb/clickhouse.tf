resource "yandex_mdb_clickhouse_cluster" "finnhub" {
  name               = "finnhub"
  environment        = "PRESTABLE"
  network_id         = yandex_vpc_network.finnhub_net.id
  security_group_ids = [ yandex_vpc_security_group.finnhub_sec_gr.id ]

  clickhouse {
    resources {
      resource_preset_id = "s2.micro"
      disk_type_id       = "network-ssd"
      disk_size          = 32
    }
  }
  
host {
    type      = "CLICKHOUSE"
    zone      = "ru-central1-b"
    subnet_id = "${yandex_vpc_subnet.finnhub_subnet.id}"
    assign_public_ip = true
  }

  database {
    name = "finnhub"
  }

  user {
    name     = "finnhub_cl"
    password = "finnhub_cl"
    permission {
      database_name = "finnhub"
    }
  }
}