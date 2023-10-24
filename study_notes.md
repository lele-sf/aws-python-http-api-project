# AWS Lambda and Python Study Notes

## Lambda Function Handler
- The handler function is the starting point of your code. It's the python function that is executed when your lambda function runs.

    ```python
    def lambda_handler(event, context):
        # TODO implement
        return {
            'statusCode': 200,
            'body': json.dumps(event)
        }
## AWS Lambda Function Parameters

AWS Lambda functions are triggered by various events and always receive two main parameters:
  - `event`: Contains information about the triggering event.
  - `context`: Provides information about the runtime environment.

### Event 
The `event` parameter typically contains information about the event that triggered the Lambda function.
- For HTTP requests, it often includes a body field with JSON data.
- An example of a JSON request body for a POST request:
    ```json
    {
        "todo": "Learn Serverless"
    }
    ```
    - This JSON data can be accessed in the Lambda function using `event['body']`.
### Context 
`context` is a Python objects that implements methods and has attributes. It's main role is to provide information about the current execution environment. Unlike `event`, the methods and properties of the `context` object remain the same regardless of the lambda was invoked or triggered. 
### Context methods

* **get_remaining_time_in_millis** – Returns the number of milliseconds left before the execution times out.

### Context properties

* **function_name** – The name of the Lambda function.
* **function_version** – The version of the function.
* **invoked_function_arn** – The Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker specified a version number or alias.
* **memory_limit_in_mb** – The amount of memory that's allocated for the function.
* **aws_request_id** – The identifier of the invocation request.
* **log_group_name** – The log group for the function.
* **log_stream_name** – The log stream for the function instance.

## Return Value
- Lambda functions can be triggered synchronously or asynchronously.
- When invoked synchronously (e.g., via API Gateway), the return value is sent back to the calling application.
- The return value is usually in a specific structure, often serialized into JSON.

## JSON Data Handling

- JSON (JavaScript Object Notation) is a lightweight data interchange format commonly used in APIs.
- In Python, we use the `json` library to work with JSON data.

### `json.loads` Function

- `json.loads` is used to parse a JSON string and convert it into a Python data structure.
- Example:
  ```python
  json_string = '{"name": "John", "age": 30}'
  python_dict = json.loads(json_string)
### `json.dumps` Function

- `json.dumps` is used to convert a Python data structure into a JSON-formatted string.
- Example:
  ```python
    python_dict = {"name": "John", "age": 30}
    json_string = json.dumps(python_dict)
