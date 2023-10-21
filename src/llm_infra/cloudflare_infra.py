# from typing import Any, Dict, Optional

# from llama_index.callbacks import CallbackManager
# from llama_index.llms.base import (
#     LLMMetadata,
# )
# from llama_index.llms.generic_utils import get_from_param_or_env
# from llama_index.llms.openai import OpenAI
# from utils.log_utils import kclogger

# DEFAULT_API_BASE = "https://knowledge-cloud-llama.msr-451.workers.dev/"
# DEFAULT_MODEL = "@cf/meta/llama-2-7b-chat-int8"


# class Cloudflare(OpenAI):
#     def __init__(
#         self,
#         model: str = DEFAULT_MODEL,
#         temperature: float = 0.1,
#         max_tokens: int = 512,
#         additional_kwargs: Optional[Dict[str, Any]] = None,
#         max_retries: int = 10,
#         api_base: Optional[str] = DEFAULT_API_BASE,
#         api_key: Optional[str] = None,
#         callback_manager: Optional[CallbackManager] = None,
#     ) -> None:
#         additional_kwargs = additional_kwargs or {}
#         callback_manager = callback_manager or CallbackManager([])

#         api_base = get_from_param_or_env("api_base", api_base, "CLOUDFLARE_API_BASE")
#         api_key = get_from_param_or_env("api_key", api_key, "ClOUDFLARE_API_KEY")

#         super().__init__(
#             model=model,
#             temperature=temperature,
#             max_tokens=max_tokens,
#             api_base=api_base,
#             api_key=api_key,
#             additional_kwargs=additional_kwargs,
#             max_retries=max_retries,
#             callback_manager=callback_manager,
#         )

#     @classmethod
#     def class_name(cls) -> str:
#         return "Cloudflare_LLM"

#     @property
#     def metadata(self) -> LLMMetadata:
#         return LLMMetadata(
#             context_window=4096,
#             num_output=self.max_tokens,
#             is_chat_model=True,
#             model_name=self.model,
#         )

#     @property
#     def _is_chat_model(self) -> bool:
#         return True
    
# class CloudflareInfra:
#     def __init__(self):
#         kclogger.info(f"CloudflareInfra::init called")
#         #TODO: get api key from secrets manager
#         self.api_key = "dummy_key"
#         self.model = "@cf/meta/llama-2-7b-chat-int8"
    
#     def getLLM(self):
#         llm = Cloudflare(model=self.model, api_key=self.api_key)
#         return llm

# CloudflareInfraInstance = CloudflareInfra()