
resource "yandex_datatransfer_endpoint" "cl-target" {
 description = "Target endpoint for ClickHouse cluster"
 name        = "cl-target"
 settings {
   clickhouse_target {
     connection {
       connection_options {
         mdb_cluster_id = yandex_mdb_clickhouse_cluster.finnhub.id
         database       = var.CLICKHOUSE_DB_NAME
         user           = var.CLICKHOUSE_DB_FINNHUB_USER
         password {
           raw = var.CLICKHOUSE_DB_FINNHUB_USER_SECRET
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
 source_id   = "dtekf9jg0b832lu4e6b0"
 target_id   = "${yandex_datatransfer_endpoint.cl-target.id}"
 type        = "INCREMENT_ONLY"

}