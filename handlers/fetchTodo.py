import json
import boto3

def fetchTodo(event, context):
    dynamodb = boto3.client('dynamodb')
    table_name = 'TodoTable'
    
    try:
        id = event['pathParameters']['id']

        response = dynamodb.get_item(
            TableName=table_name,
            Key={'id': {'S': id}}
        )
        todo_item = response.get('Item')
        if not todo_item:
            raise Exception("Todo not found")

        body = {"message": "Todo fetched successfully", "todo": todo_item}
        status_code = 200

    except Exception as e:
        body = {"error": str(e)}
        status_code = 500

    response = {
        "statusCode": status_code,
        "body": json.dumps(body)
    }

    return response