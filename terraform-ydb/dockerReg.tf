resource "yandex_container_registry" "finnhub" {
  name = "finnhub"
  folder_id = "{{ env.iac_folder }}"
  labels = {
    my-label = "finnhub"
  }

}

