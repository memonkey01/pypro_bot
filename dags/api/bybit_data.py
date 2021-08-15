# -*- coding: utf-8 -*-

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

import bybit
import pandas as pd
import time as t_time

from datetime import *
from dateutil.relativedelta import *


def get_u_timestamp(period="Day", time=1):
    TODAY = date.today()
    if period == "Week":
        time_to = TODAY - relativedelta(weeks=time)
    if period == "Day":
        time_to = TODAY - relativedelta(days=time)
    timestamp = str(time_to)
    dt = datetime.strptime(timestamp, '%Y-%m-%d')
    u_timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
    return int(u_timestamp)



def get_last_price_btc_bybit():
    client  = bybit.bybit(test=False, api_key="", api_secret="")
    demo_data = client.Market.Market_symbolInfo().result()
    btc_data = demo_data[0].get('result')[0]
    return btc_data


def get_historic_data_bybit(symbol,interval, initial_ts = 1_546_052_400):

    #symbol = 'BTCUSD'
    #interval = '1'
    #INITIAL_TS = 1_546_052_400
    
    client  = bybit.bybit(test=False, api_key="", api_secret="")
    
    master_df = pd.DataFrame(columns=['symbol', 'interval', 'open_time', 'open',
                                      'high', 'low', 'close',
                                      'volume', 'turnover', 'timestamp'])
    pagination = True
    initial_round = True
    last_time_array = [0,1]
    
    while pagination:
        if initial_round:
            raw_data = client.Kline.Kline_get(symbol=symbol, interval=interval, **{'from':initial_ts}).result()
            data = raw_data[0].get('result')
            df = pd.DataFrame(data)
            master_df = pd.concat([master_df, df])
            last_time = master_df.open_time[-1:].to_list()
            initial_round = False
        
        else:
            raw_data = client.Kline.Kline_get(symbol=symbol, interval=interval, **{'from':last_time[0]}).result()
            data = raw_data[0].get('result')
            df = pd.DataFrame(data)
            master_df = pd.concat([master_df, df])
            last_time = master_df.open_time[-1:].to_list()
            last_time_array.append(last_time[0])
            t_time.sleep(0.1)
    
            if last_time_array[-2] == last_time_array[-1]:
                break
    
    
    master_df['timestamp'] = pd.to_datetime(master_df['open_time'], unit='s')
    
    master_df = master_df.drop_duplicates(subset=['open_time'], keep='first')
    
    master_df = master_df.astype({'close':'float64','open':'float64',
                                  'high':'float64','low':'float64',
                                  'volume':'float64','turnover':'float64'})

    return master_df

if __name__ == "__main__":
    # Este es un ejemplo para obtener datos de velas de 5 min
    #test = get_historic_data_bybit('BTCUSD', '5', get_u_timestamp())
    # #print(test)
    print("ByBit Data")
