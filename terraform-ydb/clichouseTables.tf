# resource "clickhouse_table" "finnhub" {
#   database      = clickhouse_db.finnhub.finnhub
#   name    = "finnhub_table"
#   cluster       = clickhouse_db.finnhub.cluster
#   engine        = "ReplicatedMergeTree"
#   engine_params = ["'/clickhouse/{installation}/clickhouse_db.test_db_clustered.cluster/tables/{shard}/{database}/{table}'", "'{replica}'"]
#   order_by      = ["event_date", "event_type"]
#   columns {
#     name = "event_date"
#     type = "Date"
#   }
#   columns {
#     name = "event_type"
#     type = "Int32"
#   }
#   columns {
#     name = "article_id"
#     type = "Int32"
#   }
#   columns {
#     name = "title"
#     type = "String"
#   }
#   partition_by {
#     by                 = "event_date"
#     partition_function = "toYYYYMM"
#   }
# }