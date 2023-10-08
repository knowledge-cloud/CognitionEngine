import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def cognition_engine_handler(event, context):
    # TODO implement

    logger.info("Cognition Engine Lambda Handler Called")

    return {
        'statusCode': 200,
        'body': 'Hello World'
    }