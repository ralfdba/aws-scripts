import pymysql
import json

endpoint = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
ddbb = "trx"
userdb = "admin"
passdb = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

conn = pymysql.connect(host=endpoint, user=userdb, password=passdb, database=ddbb)

def lambda_handler(event,handler):
    cursor = conn.cursor()
    cursor.execute("select * from trx")
    rows = cursor.fetchall()
    
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = "application/json"
    responseObject['body'] = json.dumps(rows)

    return responseObject
