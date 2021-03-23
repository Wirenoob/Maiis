from pymongo import MongoClient
import ast
from config import data_base_url, data_base_data
connection = MongoClient(data_base_url)
def get_data():
    try:
        dbs = connection.data
        data = dbs.data
        list_of_data = data.find()
        string = ""
        for item in list_of_data:
            string = string + item['data']
        string = ast.literal_eval(string)
        return string
    except SyntaxError:
        mydb = connection['data']
        mycol = mydb['data']
        mycol.insert_one({'data' : str(data_base_data)})
        return data_base_data
    except:
    	string = {}
    	return string

def update(datas):
        datas = str(datas)
        dbs = connection.data
        data = dbs.data
        list_of_data = data.find()
        string = ""
        for item in list_of_data:
                mydb = connection['data']
                mycol = mydb['data']
                mycol.update_one(item, {'$set':{'data' : datas}})

