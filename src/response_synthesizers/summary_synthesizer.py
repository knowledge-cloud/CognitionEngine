from typing import List
from llm_infra.any_scale_infra import AnyScaleInfraInstance


class SummarySynthesizer:
    def __init__(self):
        self.anyscale_infra = AnyScaleInfraInstance

    def synthesize(self, query: str, text_list: List[str]) -> str:
        return self.summary