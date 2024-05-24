# my_second_lambda/app.py

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello from 2nd Lambda!"
    }