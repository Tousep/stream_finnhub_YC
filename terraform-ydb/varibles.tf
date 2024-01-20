variable "finnhub_stocks_tickers" {
  type    = list
  default = [ "BINANCE:BTCUSDT",
              "BINANCE:ETHUSDT",
              "BINANCE:XRPUSDT",
              "BINANCE:DOGEUSDT" ]
}
variable "token" { type= string }
