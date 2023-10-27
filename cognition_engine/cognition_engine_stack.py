from aws_cdk import Duration, Stack
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_secretsmanager
from constructs import Construct

from cognition_engine.env_constants import Env, EnvConstants


class CognitionEngineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.env_constants = EnvConstants(
            Env(self.node.try_get_context("env")))

        self.create_lambda()

    def create_lambda(self):
        self.cognition_engine_lambda = _lambda.DockerImageFunction(
            scope=self,
            id="CognitionEngineLambda",
            function_name="CognitionEngineLambda",
            code=_lambda.DockerImageCode.from_image_asset(directory=""),
            timeout=Duration.seconds(900),
            memory_size=1024,
            environment={
                "WEAVIATE_URL": self.env_constants.WEAVIATE_URL,
                "ANY_SCALE_URL": self.env_constants.ANY_SCALE_URL,
            }
        )
