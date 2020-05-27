from flask import Flask

from flask import request

from flask import jsonify

import covid19

import json
import store


app = Flask(__name__)


@app.after_request

def after_request(response):

  response.headers.add('Access-Control-Allow-Origin', '*')

  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')

  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

  return response


@app.route('/')

def welcome():

    return '''

<html>

    <head></head>

    <body>

        <h1>COVID-19 REST API</h1>

        <p>Welcome to the "COVID-19 Data" microservice endpoint.</p>

    </body>

</html>

'''


@app.route('/receiveAllPosts', methods=['GET'])

def receiveAllPosts():

    name = request.args.get('name')

    posts = store.searchTextData(name)

    return jsonify(posts)
def addImageData(imageFilename):

    cloudinary.config(

        cloud_name="drwusoh6l",

        api_key="152287666817656",

        api_secret="i2Mtj8mf--UUgG6lGmuq2O9MlFA"

        )

    uploadInfo = cloudinary.uploader.upload(imageFilename)


    return uploadInfo["url"]

   

def addTextData(data):

    db, cursor = connect()


    insert = 'INSERT INTO covid19 (name, isTotal, isRaw, metric, fromDate, toDate, url) VALUES (%s, %s, %s, %s, %s, %s, %s)'

    values = (data['name'], data['isTotal'], data['isRaw'], data['metric'], data['from'], data['to'], data['url'])

    cursor.execute(insert , values)

   

    db.commit()

    db.close()
  