import pymysql
import json
import sys

endpoint = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
ddbb = "trx"
userdb = "admin"
passdb = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

try:
    connection = pymysql.connect(host=endpoint, user=userdb, password=passdb, database=ddbb)
except:
    print("Error al conectarse a " + endpoint)
    sys.exit()

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
