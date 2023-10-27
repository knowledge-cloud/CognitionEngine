import time
from typing import List

from langchain.chains import LLMChain
# from llm_infra.cloudflare_infra import CloudflareInfraInstance
from langchain.prompts import PromptTemplate

from llm_infra.any_scale_infra import AnyScaleInfraInstance
from prompts.gyan_gpt_prompt import GYAN_GPT_PROMPT
from utils.log_utils import kclogger


class SummarySynthesizer:
    def __init__(self):
        self.anyscale_infra = AnyScaleInfraInstance
        # self.cloudflare_infra = CloudflareInfraInstance
        self.qa_prompt_template = GYAN_GPT_PROMPT

    def synthesize_summary(self, query: str, text_list: List[str]) -> str:
        start_time = time.time()
        kclogger.info(
            f"SummarySynthesizer::synthesize_summary::query: {query}")

        llm = self.anyscale_infra.getLLM()
        prompt = PromptTemplate(
            template=self.qa_prompt_template, input_variables=["context", "query"])
        llm_chain = LLMChain(prompt=prompt, llm=llm)

        summary = llm_chain.predict(query=query, context=text_list)

        kclogger.info(
            f"SummarySynthesizer::synthesize_summary::summary: {summary}")
        kclogger.info(
            f"SummarySynthesizer::synthesize_summary::time_taken: {time.time() - start_time}s")
        return summary


SummarySynthesizerInstance = SummarySynthesizer()
