from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_secretsmanager,
)
from constructs import Construct

class CognitionEngineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.create_lambda()

    def create_lambda(self):      
        self.cognition_engine_lambda = _lambda.DockerImageFunction(
                                        scope=self,
                                        id="CognitionEngineLambda",
                                        function_name="CognitionEngineLambda",
                                        code=_lambda.DockerImageCode.from_image_asset(directory=""),
                                        #handler='lambda_function.lambda_handler',
                                        timeout=Duration.seconds(900),
                                        memory_size=1024,
                                        )
