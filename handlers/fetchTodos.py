import json
import boto3

def fetchTodos(event, context):
    dynamodb = boto3.client('dynamodb')
    table_name = 'TodoTable'

    try:
        response = dynamodb.scan(TableName=table_name)
        todos = response.get('Items', [])

        body = {"message": "Todos fetched successfully", "todos": todos}
        status_code = 200

    except Exception as e:
        body = {"error": str(e)}
        status_code = 500

    response = {
        "statusCode": status_code,
        "body": json.dumps(body)
    }

    return response
