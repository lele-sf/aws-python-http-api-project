import json
import datetime
import uuid
import boto3

def addTodo(event, context):
    dynamodb = boto3.client('dynamodb')
    table_name = 'TodoTable'

    try:
        request_body = json.loads(event['body']) 
        todo = request_body.get('todo')
        if not todo:
            raise ValueError("The 'todo' field is required.")

        created_at = str(datetime.datetime.utcnow())
        todo_id = str(uuid.uuid4())

        new_todo = {
            'id': {'S': todo_id},
            'todo': {'S': todo},
            'createdAt': {'S': created_at},
            'completed': {'BOOL': False}
        }

        dynamodb.put_item(
            TableName=table_name,
            Item=new_todo
        )

        body = {"message": "Todo item added successfully", "todo": new_todo}
        status_code = 200

    except Exception as e:
        body = {"error": str(e)}
        status_code = 500

    response = {
        "statusCode": status_code,
        "body": json.dumps(body)
    }

    return response
