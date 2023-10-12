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
        environment_variables = {
            "OPENAI_API_KEY": aws_secretsmanager.Secret.from_secret_name_v2(self, "OpenAiSecretKey", secret_name="COGNITION_EGINE").secret_value.to_string(),
            "LLAMA_7B_MODEL": aws_secretsmanager.Secret.from_secret_name_v2(self, "Llama7BModel", secret_name="COGNITION_EGINE").secret_value.to_string(),
            "ANYSCALE_API_KEY": aws_secretsmanager.Secret.from_secret_name_v2(self, "AnyscaleApiKey", secret_name="COGNITION_EGINE").secret_value.to_string(),
            "WEAVIATE_URL": aws_secretsmanager.Secret.from_secret_name_v2(self, "WeaviateUrl", secret_name="COGNITION_EGINE").secret_value.to_string(),
            "WEAVIATE_API_KEY": aws_secretsmanager.Secret.from_secret_name_v2(self, "WeaviateApiKey", secret_name="COGNITION_EGINE").secret_value.to_string(),
        }
        self.cognition_engine_lambda = _lambda.DockerImageFunction(
                                        scope=self,
                                        id="CognitionEngineLambda",
                                        function_name="CognitionEngineLambda",
                                        #runtime=_lambda.Runtime.PYTHON_3_7,
                                        code=_lambda.DockerImageCode.from_image_asset("./"),
                                        #handler='lambda_function.lambda_handler',
                                        # environment={
                                        #     "Variables": environment_variables
                                        # },
                                        timeout=Duration.seconds(3),
                                        )
