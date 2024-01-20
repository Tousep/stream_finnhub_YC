variable "finnhub_stocks_tickers" {
  type    = list
  default = [ "BINANCE:BTCUSDT",
              "BINANCE:ETHUSDT",
              "BINANCE:XRPUSDT",
              "BINANCE:DOGEUSDT" ]
}
variable "YC_TOKEN" { type= string }
variable "YC_FOLDER_ID" { type= string }