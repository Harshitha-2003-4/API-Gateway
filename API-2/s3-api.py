import json

def lambda_handler(event, context):
    name = "World"
    if event.get("queryStringParameters") and event["queryStringParameters"].get("name"):
        name = event["queryStringParameters"]["name"]
        
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(f"Hello {name} from Lambda!")
    }
