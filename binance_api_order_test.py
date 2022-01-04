import ccxt
import pandas as pd
import re 
import datetime

# 계좌 접속 
binance = ccxt.binance({
    'apiKey': '값',
    'secret': '값',
})
balance = binance.fetch_balance()
# print(balance.keys())
#잔고조회
print('info:', balance['info'])
print('BNB잔고:',  balance['BNB'])
print('USDT잔고:',  balance['USDT'])

# 매수/매도 주문 
# 지정가 매매: create_limit_buy_order (), create_limit_sell_order()
# 시장가 매매: create_market_buy_order(), create_market_sell_order()

# 매수주문: limit_buy_order(종목명, 수량, 가격)
# 예제: order = binance.create_limit_buy_order('BNB/USDT', 0.1 , 511.5)
order = binance.create_limit_buy_order('BNB/USDT', 0.1 , 511.5)
print(order)

# 주문 취소: cancel_order(주문ID, 종목코드 ) 
# 예제: resp = binance.cancel_order(3518330818, 'BNB/USDT')
resp = binance.cancel_order(3518330818, 'BNB/USDT')
print(resp)