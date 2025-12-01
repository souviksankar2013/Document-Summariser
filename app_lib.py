import boto3

def get_summary(doc_bytes, input_text):

    # Determine file format (optional; you can also pass it in)
    file_format = "pdf"  # adjust if needed based on upload

    doc_message = {
        "role": "user",
        "content": [
            {
                "document": {
                    "name": "Uploaded Document",
                    "format": file_format,
                    "source": {
                        "bytes": doc_bytes
                    }
                }
            },
            {"text": input_text}
        ]
    }
    
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')
    
    response = bedrock.converse(
        modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        messages=[doc_message],
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0
        },
    )
    
    return response['output']['message']['content'][0]['text']
