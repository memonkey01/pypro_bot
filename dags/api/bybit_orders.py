# -*- coding: utf-8 -*-

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

import bybit 



def set_buy_order(BYBIT_API_KEY, BYBIT_API_SECRET, ORDER_SIZE_DEFAULT):
    client = bybit.bybit(test=True, api_key=BYBIT_API_KEY, api_secret=BYBIT_API_SECRET)
    long = client.Order.Order_new(side="Buy",symbol="BTCUSD",order_type="Market",qty=ORDER_SIZE_DEFAULT,time_in_force="GoodTillCancel").result()    
    positions = client.Positions.Positions_myPosition(symbol="BTCUSD").result()
    return positions[0]['result']

def set_sell_order(BYBIT_API_KEY, BYBIT_API_SECRET, ORDER_SIZE_DEFAULT):
    client = bybit.bybit(test=True, api_key=BYBIT_API_KEY, api_secret=BYBIT_API_SECRET)
    short = client.Order.Order_new(side="Sell",symbol="BTCUSD",order_type="Market",qty=ORDER_SIZE_DEFAULT,time_in_force="GoodTillCancel").result()    
    positions = client.Positions.Positions_myPosition(symbol="BTCUSD").result()
    return positions[0]['result']

if __name__ == '__main__':

    #from settings.config import BYBIT_API_KEY, BYBIT_API_SECRET, ORDER_SIZE_DEFAULT
    #print(set_buy_order(BYBIT_API_KEY, BYBIT_API_SECRET, ORDER_SIZE_DEFAULT))
    #print("-------- EJECUTAMOS POSICIÓN LARGA")
    #print(set_sell_order(BYBIT_API_KEY, BYBIT_API_SECRET, ORDER_SIZE_DEFAULT))
    print("-------- EJECUTAMOS POSICIÓN CORTA")
