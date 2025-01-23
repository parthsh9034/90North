 Create AWS Lambda Functions

Log in to the AWS Management Console: Go to the AWS Lambda service.
Create Functions: Create two new Lambda functions:
For the "Add Two Numbers" function, choose "Python 3.9" as the runtime.
For the "Store File in S3" function, also choose "Python 3.9" as the runtime.
Upload Code:
Upload the respective Python code files (add_numbers.py and s3_file_upload.py) to the corresponding Lambda functions.
Configure Environment Variables:
For the "Store File in S3" function, you might need to configure environment variables like the S3 bucket name to avoid hardcoding them in the code.
2. Test the "Add Two Numbers" Function

Create a Test Event: In the Lambda function's configuration, create a test event with the following JSON structure:

JSON

{
    "num1": 10,
    "num2": 5
}
Test the Function: Click the "Test" button. The function should execute and return the sum of the two numbers (15 in this case).

3. Test the "Store File in S3" Function

Create a Test Event: Create a test event with the following structure (replace with actual file data):

JSON

{
    "file_name": "example.txt", 
    "file_data": "This is an example file." 
}
Test the Function: Click the "Test" button. The function should upload the file to the specified S3 bucket.

4. Invoke Functions (Optional)

You can invoke these Lambda functions from other AWS services (e.g., API Gateway, EventBridge) or directly using the AWS CLI or SDKs.
Important Considerations:

IAM Permissions: Ensure that the Lambda functions have the necessary IAM permissions to perform their actions. For example, the "Store File in S3" function needs permissions to write objects to the S3 bucket.
Error Handling: Implement robust error handling in your Lambda functions to gracefully handle potential issues like invalid input, network errors, or S3 access errors.
Security: Follow AWS security best practices, such as using least privilege principles and regularly reviewing and updating IAM permissions.
Additional Notes:

For more complex scenarios, you might want to use AWS services like API Gateway to create RESTful APIs that trigger your Lambda functions.
Consider using Lambda layers to manage dependencies and reduce function size.