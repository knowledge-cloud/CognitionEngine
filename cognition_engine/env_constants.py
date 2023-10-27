from enum import Enum


class Env(Enum):
    PROD = "PROD"
    GAMMA = "GAMMA"


class EnvConstants:
    def __init__(self, env: Env):
        match env:
            case Env.PROD:
                self.WEAVIATE_URL = "https://not-configured.weaviate.network"
                self.ANY_SCALE_URL = "https://api.endpoints.anyscale.com/v1"
            case Env.GAMMA:
                self.WEAVIATE_URL = "https://test-cognition-engine-bwftey9k.weaviate.network"
                self.ANY_SCALE_URL = "https://api.endpoints.anyscale.com/v1"
            case default:
                raise Exception("Invalid env")
