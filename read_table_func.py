import pandas as pd
import numpy as np
from datetime import datetime
from pymongo import MongoClient
import json
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client.bakery_house

def read_transactions_table():
    # client = MongoClient('localhost', 27017)
    # db = client.bakery_house

    # view data table sales
    sales = list(db.sales.find({}, {'_id': False}))

    # convert to dataframe
    df_transactions = pd.DataFrame(sales)
    df_transactions['datetime'] = pd.to_datetime(df_transactions['datetime'])
    return df_transactions


def read_bakery_table():
    # client = MongoClient('localhost', 27017)
    # db = client.bakery_house

    # view data table bakery
    bakery = list(db.bakery.find({}, {'_id': False}))

    # convert to dataframe
    df_bakery = pd.DataFrame(bakery)
    return df_bakery

def read_bakery_table2():
    collection = db.bakery
    df_bakery2 = pd.DataFrame(list(collection.find()))
    return df_bakery2

def read_branch_table():
    # client = MongoClient('localhost', 27017)
    # db = client.bakery_house

    # view data table branch
    branch = list(db.branches.find({}, {'_id': False}))

    # convert to dataframe
    df_branch = pd.DataFrame(branch)
    return df_branch

def read_branch_table2():
    collection = db.branches
    df_branch2 = pd.DataFrame(list(collection.find()))
    return df_branch2

###############################
def df_month_branch_sales_func():
    sales = list(db.sales.find({}, {'_id': False}))
    # convert to dataframe
    df = pd.DataFrame(sales)
    df['datetime'] = pd.to_datetime(df['datetime'])
    df_month_branch_sales = df.total_price.groupby([df['datetime'].dt.year, df['datetime'].dt.month, df['branch']]).sum()
    df_month_branch_sales.index.names = ['year', 'month', 'branch']
    df_month_branch_sales = pd.DataFrame(df_month_branch_sales)
    df_month_branch_sales.reset_index(inplace=True)
    df_month_branch_sales.columns = ['year', 'month', 'branch', 'sales']
    # convert month number to month name
    df_month_branch_sales['month'] = df_month_branch_sales['month'].apply(lambda x: datetime.strptime(str(x), "%m").strftime("%B"))
    return df_month_branch_sales

