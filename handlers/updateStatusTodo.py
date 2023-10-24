import json
import boto3

def updateStatusTodo(event, context):
    dynamodb = boto3.client('dynamodb')
    table_name = 'TodoTable'

    try:
        id = event['pathParameters']['id']
        request_body = json.loads(event['body'])
        completed = request_body.get('completed')
        if completed is None:
            raise ValueError("The 'completed' field is required in the request body.")

        update_expression = 'SET completed = :completed'
        expression_attribute_values = {':completed': {'BOOL': completed}}

        dynamodb.update_item(
            TableName=table_name,
            Key={'id': {'S': id}},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )

        body = {"message": "Todo item updated successfully", "completed": completed}
        status_code = 200

    except Exception as e:
        body = {"error": str(e)}
        status_code = 500

    response = {
        "statusCode": status_code,
        "body": json.dumps(body)
    }

    return response

