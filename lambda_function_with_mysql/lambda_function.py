import pymysql
import json

endpoint = "api.cluster-cpn85tfypxsq.us-east-1.rds.amazonaws.com"
ddbb = "trx"
userdb = "admin"
passdb = "**curso2022"

conn = pymysql.connect(endpoint, user=userdb, passwd=passdb, db=ddbb)

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
