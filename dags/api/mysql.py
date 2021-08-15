import mysql.connector

class MySQL():
    """Class to interact with MySQL
    """
    def __init__(self, CONFIG_MYSQL):
        self.conn = mysql.connector.connect(**CONFIG_MYSQL)

    def __repr__(self):
        return f'MySQL connection handler'

    def __str__(self):
        return f'MySQL connection handler'

    def execute_qry(self, query):
        """
        Execute Query

        Args:
            query (str): Query to be executed

        Returns:
            None: 
        """
        if (self.conn.is_connected() == False ):
            self.conn.reconnect()
            
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        cursor.close()
    
    def close_conn(self):
        """ Always close the connection =)
        """
        self.conn.close()

def qry_create_order(message):
    """
    Create query to add processed files to RawProcess Table
    
    Args:
        df (pd.DataFrame): DataFrame with all processed files
        to be added in the DB

    Returns:
        str: Query
    """

    initial_q = """INSERT INTO orders_created
    (timestamp,order_type,price_taken,order_amount,algo_strategy)
    VALUES
    """
    values_q = """("{}","{}","{}","{}","{}")""".format(*message)
    
    end_q = """ ON DUPLICATE KEY UPDATE
            timestamp = values(timestamp),
            order_type = values(order_type),
            price_taken = values(price_taken),
            order_amount = values(order_amount),
            algo_strategy = values(algo_strategy);"""
            
    query = initial_q + values_q + end_q

    return query