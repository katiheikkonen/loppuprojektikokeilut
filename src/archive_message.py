#  Funktio asiakaspalautteiden arkistointiin

import boto3
s3 = boto3.resource("s3")

def archive(event, context):
    #  Haetaan uuden tiedoston nimi Step Functionin käynnistävästä tapahtuman inputista
    message_to_archive = event['resources'][0]['ARN'] #  palautus muodossa "arn:aws:s3:::username-sfn-tutorial-2/test.png"
    bucket_name = ['requestParameters']['bucketName']
    # "customer-review-loppuprojekti-12345", tai voi laittaa enviroment variableksi

    #  keskeneräinen, palaan/palataan, kun S3 - Step Function triggeröinti selvillä ja pystyy testaamaan paremmin
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=json.dumps(sisalto))