import json

#  S3 laukaisee tämän Lambdan
#  Lambda lähettää saadun palautteen Amazon Comprehendille analysoitavaksi Sentimental Analysis-työkalun kautta
import boto3

# s3 = boto3.client("s3")
comprehend = boto3.client("comprehend")
s3 = boto3.resource('s3')


def sentimental_analysis(event, context):

    #  NÄIDEN HAKEMINEN STEP FUNCTIONS TRIGGERISTÄ

    # Poimitaan S3sta tulevasta eventistä..
    s3_trigger = event['Records']
    # Uuden tiedoston nimi, sekä
    s3_filename = s3_trigger[0]['s3']['object']['key']
    # bucketin nimi
    s3_bucket_name = s3_trigger[0]['s3']['bucket']['name']

    # haettu objekti:
    obj = s3.Object(s3_bucket_name, s3_filename)
    # tiedoston sisältä
    m_body = obj.get()['Body']._raw_stream.readline()
    viesti = json.loads(m_body)

    # sisällön message kenttä:
    message = viesti['message']
    print(message)

    # Extracting sentiments using comprehend
    reply = comprehend.detect_sentiment(Text=message, LanguageCode="en")

    # + potentiaalista debugausta varten retry-attemps kenttä:
    retry_attemps = reply['ResponseMetadata']['RetryAttempts']

    return {
        "statusCode": 200,
        "body": json.dumps(reply)
    }