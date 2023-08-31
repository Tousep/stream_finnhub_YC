resource "yandex_container_registry" "finnhub" {
  name = "finnhub"
  folder_id = "b1gh11gr471pupbosu5q"
  labels = {
    my-label = "finnhub"
  }

}

