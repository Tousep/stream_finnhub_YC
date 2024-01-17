terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  service_account_key_file = file("key.json")
  folder_id = "{{ env.iac_folder }}"
  zone = "ru-central1-b"
}
