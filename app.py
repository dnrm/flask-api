from flask import Flask
from uuid import uuid4
import json


import pymongo

conn_str = ''

client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/example')
def example():
    return json.dumps({'_id': uuid4(), 'name': 'Daniel'})


@app.route('/users')
def users():
    try:
        db = client["instagram-api-app"]
        items = db.usernames

        results = []

        for doc in items.find():
            results.append(doc)

        print(results)
        return {
            "res": str(results)
        }
    except Exception as e:
        print(e)
        return "no c q paso"


if __name__ == '__main__':
    app.run()
