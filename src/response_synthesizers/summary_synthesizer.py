from typing import List
from llama_index import ServiceContext
from llama_index.response_synthesizers import Refine
from llm_infra.any_scale_infra import AnyScaleInfraInstance
import os
from utils.log_utils import kclogger


class SummarySynthesizer:
    def __init__(self):
        self.anyscale_infra = AnyScaleInfraInstance

    def synthesize_summary(self, query: str, text_list: List[str]) -> str:
        kclogger.info(f"SummarySynthesizer::synthesize_summary summarizing for query: {query}")
        llm = self.anyscale_infra.getLLM(os.environ.get("LLAMA_7B_MODEL"))
        service_context = ServiceContext.from_defaults(llm=llm)
        summarizer = Refine(service_context=service_context, verbose=True)
        summary = summarizer.get_response(query_str=query, text_chunks=text_list)
        kclogger.info(f"SummarySynthesizer::synthesize_summary summary: {summary}")
        return summary
    
SummarySynthesizerInstance = SummarySynthesizer()
synthesize_summary = SummarySynthesizerInstance.synthesize_summary