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
  folder_id = "b1gh11gr471pupbosu5q"
  zone = "ru-central1-b"
}