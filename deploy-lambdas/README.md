# AWS SAM Application with Unit Testing

This README provides a detailed, step-by-step guide for developing and testing an AWS Serverless Application Model (SAM) application using Python's built-in `unittest` module for unit testing your Lambda functions. We'll create the project structure from scratch and ensure that all necessary steps are covered.

## Step 1: Set up your SAM Application Directory

1. **Create a new directory for your SAM application**:
   
   ```
   mkdir deploy-lambdas
   cd deploy-lambdas
   ```

2. **Create the `template.yaml` file**:
   
   This file is the SAM template that defines your serverless resources, including Lambda functions and API Gateway. Create a new file named `template.yaml` and add the following content:

   ```yaml
   AWSTemplateFormatVersion: '2010-09-09'
   Transform: AWS::Serverless-2016-10-31
   Description: A simple Lambda function

   Resources:
     HelloWorldFunction:
       Type: AWS::Serverless::Function
       Properties:
         CodeUri: my_lambda/
         Handler: app.lambda_handler
         Runtime: python3.9
   ```

3. **Create a directory for your Lambda function**:
   
   ```
   mkdir hello_world
   ```

4. **Add your Lambda function code**:
   
   Inside the `hello_world/` directory, create a new file named `app.py` and add your Lambda function code. For example:

   ```python
   # hello_world/app.py

   def lambda_handler(event, context):
       return {
           "statusCode": 200,
           "body": "Hello from Lambda!"
       }
   ```

5. **Create a directory for tests**:
   
   ```
   mkdir tests
   ```

## Step 2: Write Unit Tests

1. **Create a test file**:
   
   Inside the `tests/` directory, create a new Python file for your unit tests. For example, `tests/test_hello_world.py`.

   ```python
   # tests/test_hello_world.py

   import unittest
   from unittest.mock import patch
   from hello_world import app

   class TestHelloWorldFunction(unittest.TestCase):
       def setUp(self):
           self.event = {}
           self.context = {}

       def test_lambda_handler(self):
           response = app.lambda_handler(self.event, self.context)
           self.assertEqual(response["statusCode"], 200)
           self.assertEqual(response["body"], "Hello from Lambda!")

   if __name__ == "__main__":
       unittest.main()
   ```

   In this example, we create a `TestHelloWorldFunction` class that inherits from `unittest.TestCase`. The `setUp` method sets up the `event` and `context` objects for testing. The `test_lambda_handler` method invokes the Lambda function and asserts the expected response.


2. **Write additional test cases**:
   Add more test cases to the `TestHelloWorldFunction` class or create additional test classes and files as needed to cover different scenarios and edge cases for your Lambda functions.

## Step 3: Run Tests Locally

You can run your tests locally by executing the test file from the command line:

```
python tests/test_hello_world.py
```

This command will run all the test cases defined in the `test_hello_world.py` file and display the results in the console.

## Step 4: Integration Testing with `sam local`

AWS SAM provides the `sam local` commands for local testing, which can be useful for integration testing. You can invoke your Lambda functions locally with different event payloads and test their integration with other AWS services (e.g., API Gateway, DynamoDB) using the `sam local` commands:

1. Install Docker (if not already installed):

The sam local invoke command requires Docker to be installed and running on your machine. If you haven't installed Docker yet, download and install it from the official Docker website: https://www.docker.com/get-started

2. Start Docker service:

After installing Docker, make sure the Docker service is running on your machine.

On Windows and macOS, you can usually find the Docker application in the system tray or applications menu and start the Docker service from there.
On Linux, you may need to start the Docker service manually using the appropriate command for your distribution (e.g., sudo systemctl start docker on Ubuntu/Debian).

3. Local invocation:

Once Docker is running, you can use the sam local invoke command to invoke your Lambda function locally with sample event data:

```
sam local invoke <function-name> --event events/event.json
sam local start-api
```

Replace events/event.json with a JSON file containing the event data you want to test with. This command will invoke the HelloWorldFunction Lambda function locally, using the event data specified in the JSON file.

## Deploying Your Application

When you're ready to deploy your serverless application to the AWS cloud, use the `sam deploy` command:

```
sam deploy --guided
```

The `--guided` flag prompts you to provide the required deployment configurations, such as the AWS region and stack name.

During the deployment process, SAM creates or updates an AWS CloudFormation stack with the resources defined in your `template.yaml` file. It uploads your Lambda function code and dependencies to AWS Lambda and configures other resources like API Gateway.

After a successful deployment, SAM will output the relevant information about your deployed resources, such as the API Gateway endpoint URLs and Lambda function ARNs.

## Cleaning Up

If you want to remove the resources created by your SAM application, you can use the `sam delete` command:

```
sam delete
```

This command will delete the AWS CloudFormation stack and all associated resources, effectively removing your deployed serverless application from the AWS cloud.

## Additional Resources

- [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- [SAM CLI Command Reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html)
- [SAM Template Specification](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification.html)
