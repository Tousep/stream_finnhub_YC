variable "finnhub_stocks_tickers" {
  type    = list
  default = [ "BINANCE:BTCUSDT",
              "BINANCE:ETHUSDT",
              "BINANCE:XRPUSDT",
              "BINANCE:DOGEUSDT" ]
}
variable "YC_TOKEN" {
  type= string 
  sensitive = true
  }
variable "YC_FOLDER_ID" {
  type= string 
  sensitive= true
  }
variable "YC_CONTAINER_REGISTRY" {
  type= string 
  sensitive= true
  }
variable "YC_SERVICE_ACCOUNT_ID" {
  type= string 
  sensitive= true
  }
variable "CLICKHOUSE_DB_FINNHUB_USER" {
  type= string 
  sensitive= true 
  }
variable "CLICKHOUSE_DB_FINNHUB_USER_SECRET" {
  type= string 
  sensitive= true
  }
variable "CLICKHOUSE_DB_NAME" {
  type= string 
  sensitive= true
  }
variable "FINNHUB_API_KEY" {
  type= string 
  sensitive= true
  }
variable "KAFKA_FINNHUB_TOPIC" {
  type= string 
  sensitive= true
  }
variable "KAFKA_USER_CONSUMER" {
  type= string 
  sensitive= true
  }
variable "KAFKA_USER_PRODUCER" {
  type= string 
  sensitive= true
  }
variable "KAFKA_USER_SECRET_CONSUMER" {
  type= string 
  sensitive= true
  }
variable "KAFKA_USER_SECRET_PRODUCER" {
  type= string 
  sensitive= true
  }
variable "S3_TERRAFORM" {
  type= string 
  sensitive= true
  }
