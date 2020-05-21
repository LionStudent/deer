...

import cloudinary

import cloudinary.uploader

...

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