import json
import base64
import boto3

runtime = boto3.client('runtime.sagemaker')

ENDPOINT_NAME = "image-classification-2022-05-14-07-34-42-730"
runtime = boto3.Session().client('sagemaker-runtime')

def lambda_handler(event, context):

    # Decode the image data
    image_data = base64.b64decode(event['body']['image_data'])

    # Make a prediction:
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME, ContentType = 'image/png', Body = image_data)

    # We return the data back to the Step Function    
    event["inferences"] = json.loads(response['Body'].read().decode())
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }