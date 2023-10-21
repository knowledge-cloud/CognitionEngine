# test function it locally
# python3 src/test.py

# load the lambda function locally and test it
# pip install python-lambda-local
# python-lambda-local -f lambda_handler src/lambda_function.py src/test-event.json 

import lambda_function


response = lambda_function.lambda_handler(
    {
      "eventType": "RETRIEVAL",
      "data": {
        "query": "what is NDMA?",
        "knowledgeBaseIndex": "KCIndex"
      }
    },
    "test"
)

print(response)