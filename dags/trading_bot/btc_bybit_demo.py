import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)


def run_bollinger_strategy():
    from settings.config import BYBIT_API_KEY, BYBIT_API_SECRET, ORDER_SIZE_DEFAULT, CONFIG_MYSQL
    from api.mysql import MySQL, qry_create_order
    from api.bybit_data import get_u_timestamp, get_historic_data_bybit
    from api.bybit_orders import set_buy_order, set_sell_order
    from strategies.bolliger_bands import apply_mean_reverse
    import pandas as pd

    STRATEGY = "bybit_demo_bollinger"

    mysql = MySQL(CONFIG_MYSQL)

    
    # CARGAR DATOS
    data = get_historic_data_bybit('BTCUSD', '5', get_u_timestamp())

    # EJECUTAR ESTRATEGIA
    signal, data_bands = apply_mean_reverse(data, 30)

    print("--------- DATA FINAL --------")
    print(data_bands.tail())

    # EJECUTAR REGLAS DE VALIDACION
        # Si hay alcista
        # Si tenemos saldo

    # EJECTUAR ORDEN DINAMICA 
        # Modificar el tamaño de nuestra orden
        
    # COLOCAR ORDENES
    if signal == True:
        set_buy_order(BYBIT_API_KEY, BYBIT_API_SECRET, ORDER_SIZE_DEFAULT)
        print("--------- ORDEN LARGA ----------")
        message = (pd.datetime.now(), 'LONG', data.close.iloc[-1], ORDER_SIZE_DEFAULT, STRATEGY )

    if signal == False:
        set_sell_order(BYBIT_API_KEY, BYBIT_API_SECRET, ORDER_SIZE_DEFAULT)
        print("--------- ORDEN CORTA ----------")
        message = (pd.datetime.now(), 'SHORT', data.close.iloc[-1], ORDER_SIZE_DEFAULT, STRATEGY )

    if signal is None:
        message = (pd.datetime.now(), 'NULL', data.close.iloc[-1], 0, STRATEGY )

        #raise("SIN ORDEN EJECUTADA")
    
    # INSERTAR EN MYSQL
    query = qry_create_order(message)
    mysql.execute_qry(query)
    mysql.close_conn()
    print("--------- DATOS INSERTADOS EN MYSQL ----------")

    # IMPRIMIR OUTPUT FINAL
    print(message)

