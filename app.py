from flask import Flask,request
import mongo_client
import json
app = Flask(__name__)
@app.route('/api/data/<database>/<collection>', methods=['GET', 'POST'])
def api(database,collection):
    if request.method=='post':
       body = request.body()
       json.load(body)#json转字典
       db = mongo_client.client[database]
       account = db[collection]
       account.insert_one(body)
if __name__ == '__main__':
    app.run()
