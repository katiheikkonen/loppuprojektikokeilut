import uuid
import boto3
dynamodb = boto3.resource('dynamodb')

def put_to_dynamodb():

    # Tallennetaan sortattu Comprehend data DynamoDB tauluun:
    table = dynamodb.Table("sentiment_data_analysis_table")  # Nimi kovakoodattuna

    # Luodaan item/ Rivi, johon poimitaan data sentimentistä tulleesta datasta ja joka tallennetaan Dynamoon:
    item = {
        "id": str(uuid.uuid4()),
        "sentiment": reply['Sentiment'],
        "positive": str(reply['SentimentScore']['Positive']),
        "negative": str(reply['SentimentScore']['Negative']),
        "neutral": str(reply['SentimentScore']['Neutral']),
        "mixed": str(reply['SentimentScore']['Mixed']),
        "time": str(reply['ResponseMetadata']['HTTPHeaders']['date'])
    }
    # Tallennus:
    table.put_item(Item=item)

    print(item)

    # Luodaan Response, jonka lambda näyttää suorituksen jälkeen:
    response = {
        "statusCode": 200,
        "body": json.dumps(item)}

    return response