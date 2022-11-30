import pandas as pd
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