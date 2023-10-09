import os
from llama_index.llms.anyscale import Anyscale

class AnyScaleInfra:
    def __init__(self):
        api_key = os.environ.get("ANYSCALE_API_KEY")
    
    def getLLM(self, model: str):
        llm = Anyscale(model=model, api_key=self.api_key)
        return llm