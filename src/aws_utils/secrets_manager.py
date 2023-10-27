import json

import boto3
from botocore.exceptions import ClientError

from utils.log_utils import kclogger


class SecretsManager:
    def __init__(self) -> None:
        kclogger.info(f"SecretsManager::init called")
        self.secret_name = "COGNITION_EGINE"
        self.client = boto3.session.Session().client(
            service_name='secretsmanager',
            region_name="ap-south-1"
        )

    def get_secret(self, secret_key: str) -> str:
        try:
            get_secret_value_response = self.client.get_secret_value(
                SecretId=self.secret_name)
        except ClientError as e:
            kclogger.error(
                f"SecretsManager::get_secret failed with {e.response}")
            raise e
        else:
            if 'SecretString' in get_secret_value_response:
                kclogger.info(f"SecretsManager::get_secret succeeded")
                secret_string = get_secret_value_response['SecretString']
                secret_json = json.loads(secret_string)
                return secret_json[secret_key]
            else:
                raise Exception(
                    "SecretsManager::get_secret failed with no secret string")


SecretsManagerInstance = SecretsManager()
get_secret = SecretsManagerInstance.get_secret
