import json

def lambda_handler(event, context):
    """
    This function adds two numbers and returns the result.

    Args:
        event: The event dictionary.
        context: The context dictionary.

    Returns:
        A dictionary containing the sum of the two numbers.
    """
    try:
        num1 = event['num1']
        num2 = event['num2']
        sum = num1 + num2
        return {
            'statusCode': 200,
            'body': json.dumps({'sum': sum})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }