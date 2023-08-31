resource "yandex_datatransfer_endpoint" "cl-source" {
 description = "Source endpoint for Kafka cluster"
 name        = "cl-source"
 settings {
   kafka_source {
     connection {
       connection_options {
         mdb_cluster_id = yandex_mdb_kafka_connect.finnhub.id
         topic       = "finnhub_market"
         user           = "finnhub_c"
         password {
           raw = "finnhub_c"
         }
       }
     }
   }
 }
}

resource "yandex_datatransfer_endpoint" "cl-target" {
 description = "Target endpoint for ClickHouse cluster"
 name        = "cl-target"
 settings {
   clickhouse_target {
     connection {
       connection_options {
         mdb_cluster_id = yandex_mdb_clickhouse_cluster.finnhub.id
         database       = "finnhub"
         user           = "finnhub_cl"
         password {
           raw = "finnhub_cl"
         }
       }
     }
     cleanup_policy = "CLICKHOUSE_CLEANUP_POLICY_DROP"
   }
 }
}

resource "yandex_datatransfer_transfer" "finnhub-transfer" {
 description = "Transfer from the Managed Service for Kafka to the Managed Service for ClickHouse"
 name        = "transfer-from-mkf-to-mch"
 source_id   = "dtedeebmc6jbkj3rdfd0"
 target_id   = "${yandex_datatransfer_endpoint.cl-target.id}"
 type        = "INCREMENT_ONLY"
}