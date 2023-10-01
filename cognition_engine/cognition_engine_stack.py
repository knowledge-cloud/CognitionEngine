from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct

class CognitionEngineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cognition_engine_lambda = _lambda.Function(
                                        self,
                                        "CognitionEngineLambda",
                                        runtime=_lambda.Runtime.PYTHON_3_7,
                                        code=_lambda.Code.from_asset("src/cognition_engine_lambda"),
                                        handler='cognition_engine_lambda.cognition_engine_handler',
                                        )
