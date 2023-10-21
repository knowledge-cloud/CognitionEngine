from utils.log_utils import kclogger
from typing import List
from llm_infra.any_scale_infra import AnyScaleInfraInstance
# from llm_infra.cloudflare_infra import CloudflareInfraInstance
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import time


class SummarySynthesizer:
    def __init__(self):
        self.anyscale_infra = AnyScaleInfraInstance
        # self.cloudflare_infra = CloudflareInfraInstance
        self.qa_prompt_template = """
            You are an expert Q&A system that is trusted around the world.
            Always answer the query using the provided context information, and not prior knowledge.
            Some rules to follow:
            1. Never directly reference the given context in your answer.
            2. Avoid statements like 'Based on the context, ...' or 'The context information ...' or anything along those lines.

            Here is the context information:
            {context}

            Here is the query:
            {query}
            
            Answer:
        """

    def synthesize_summary(self, query: str, text_list: List[str]) -> str:
        start_time = time.time()
        kclogger.info(f"SummarySynthesizer::synthesize_summary summarizing for query: {query}")
        llm = self.anyscale_infra.getLLM()
        prompt = PromptTemplate(template=self.qa_prompt_template, input_variables=["context", "query"])
        llm_chain = LLMChain(prompt=prompt, llm=llm)
        summary = llm_chain.predict(query=query, context=text_list)
        kclogger.info(f"SummarySynthesizer::synthesize_summary returning summary: {summary}")
        kclogger.info(f"SummarySynthesizer::synthesize_summary took {time.time() - start_time} seconds")
        return summary
    
SummarySynthesizerInstance = SummarySynthesizer()
synthesize_summary = SummarySynthesizerInstance.synthesize_summary