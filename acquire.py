import pandas as pd
import numpy as np
import os
from env import host, user, password

def get_connection(db, user=user, host=host, password=password):
    '''
    'hacking into the mainframe'
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def telco_churn():
    sql_query = """
                SELECT * FROM customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    df.to_csv('telco_df.csv')
    return df

def new_telco_data():
    #Let's pull in telco data, ALL of it.
    sql_query = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    return df
    
def get_telco_data(cached=False):
    '''
    If there is already a csv locally saved
    '''
    if cached or os.path.isfile('telco_df.csv') == False:
        df = new_telco_data()
    else:
        df = pd.read_csv('telco_df.csv', index_col=0)
    return df
