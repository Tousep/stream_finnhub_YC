resource "yandex_container_registry" "finnhub" {
  name = "finnhub"
  folder_id = var.YC_FOLDER_ID
  labels = {
    my-label = "finnhub"
  }

}

