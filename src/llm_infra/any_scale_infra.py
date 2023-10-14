from utils.log_utils import kclogger
from llama_index.llms.anyscale import Anyscale
from aws_utils.secrets_manager import get_secret

class AnyScaleInfra:
    def __init__(self):
        kclogger.info(f"AnyScaleInfra::init called")
        self.api_key = get_secret('AnyscaleApiKey')
        self.model = 'meta-llama/Llama-2-7b-chat-hf'
    
    def getLLM(self):
        llm = Anyscale(model=self.model, api_key=self.api_key)
        return llm

AnyScaleInfraInstance = AnyScaleInfra()
