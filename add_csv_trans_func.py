# fuction add csv file to mongodb if can not add to mongodb print error
def add_csv_trans_to_mongodb(csv_file):
    import pandas as pd
    from pymongo import MongoClient

    client = MongoClient('localhost', 27017)
    db = client.bakery_house

    try:
        # read csv file
        df = pd.read_csv(csv_file)

        df.datetime = pd.to_datetime(df.datetime)
        df.order_id = df.order_id.astype(str)
        df.branch = df.branch.astype(str)
        df.product_id = df.product_id.astype(str)
        df.quantity = df.quantity.astype(int)
        df.unit_price = df.unit_price.astype(int)
        df.total_price = df.total_price.astype(int)

        # convert to json
        data = df.to_dict('records')

        # insert data to mongodb
        db.sales.insert_many(data)
        print('Add csv file to mongodb successfully')
    except:
        print('Error: can not add csv file to mongodb')
