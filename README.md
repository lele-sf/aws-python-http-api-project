# AWS Python HTTP API Project

This README provides an overview of an AWS Python HTTP API project. The project is configured using the Serverless Framework and consists of AWS Lambda functions and a DynamoDB table for managing a to-do list.

## Serverless Configuration

The project's configuration is defined in the `serverless.yml` file, and it includes various sections:

### Service

- **Service Name:** `aws-python-http-api-project`: This is the name of your Serverless service.
- **Framework Version:** 3: Specifies the version of the Serverless Framework being used.

### Provider

- **Name:** AWS: Indicates that the project will be deployed on AWS.
- **Runtime:** Python 3.11: Specifies the runtime environment for the Lambda functions.
- **Region:** `us-west-1`: Specifies the AWS region where the project will be deployed.
- **IAM Role Statements:** This section defines permissions for DynamoDB actions. You need to replace `YourDynamodbTableArn` with the actual ARN of your DynamoDB table.

### Functions

The project includes four Lambda functions:

1. **addTodo**: Adds a to-do item to the DynamoDB table. It is triggered by an HTTP POST request to the root path (`/`).

2. **fetchTodos**: Retrieves all to-do items from the DynamoDB table. It is triggered by an HTTP GET request at the path `/todos`.

3. **fetchTodo**: Fetches a single to-do item from the DynamoDB table based on the provided `id`. It is triggered by an HTTP GET request at the path `/todo/{id}`.

4. **updateStatusTodo**: Updates the completion status of a to-do item in the DynamoDB table based on the provided `id`. It is triggered by an HTTP PUT request at the path `/todo/{id}`.

### Resources

- **DynamoDB Table: TodoTable**: This section defines a DynamoDB table named `TodoTable` with specified attributes and a key schema.

## How to Deploy

To deploy this project, follow these steps:

1. Clone this repository.
2. Navigate to the project directory.
3. Run the command `sls deploy` to deploy the project to AWS.

## How to Use

Once the project is deployed, you can use the HTTP API to interact with the to-do list:

- To add a to-do item, send a POST request to the root path (`/`) with a JSON body containing the to-do item.
- To fetch all to-do items, send a GET request to `/todos`.
- To fetch a single to-do item, send a GET request to `/todo/{id}`, where `{id}` is the unique identifier of the to-do item.
- To update the completion status of a to-do item, send a PUT request to `/todo/{id}` with a JSON body containing the `completed` field.

## Additional Information

For more details and customization options, refer to the [Serverless Framework documentation](https://www.serverless.com/framework/docs).
