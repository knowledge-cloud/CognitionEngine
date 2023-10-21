from utils.log_utils import kclogger
from langchain.llms.anyscale import Anyscale
from aws_utils.secrets_manager import get_secret

class AnyScaleInfra:
    def __init__(self):
        kclogger.info(f"AnyScaleInfra::init called")
        self.api_key = get_secret('AnyscaleApiKey')
        self.model = 'meta-llama/Llama-2-7b-chat-hf'
        self.api_base_url = 'https://api.endpoints.anyscale.com/v1'
    
    def getLLM(self):
        llm = Anyscale(model=self.model, anyscale_api_key=self.api_key, anyscale_api_base=self.api_base_url)
        return llm

AnyScaleInfraInstance = AnyScaleInfra()
