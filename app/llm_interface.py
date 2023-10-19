from llm.llm_blueprint import LLMFactory
from llm.ctransformer_wrapper import CTRANSFORMERS_LLM
from llm.llamacpp_wrapper import LLAMA_CPP_BASE

from template import qpr_data

llm_factory = LLMFactory()
llm_factory.register_type("ctransformer", CTRANSFORMERS_LLM)
llm_factory.register_type("llamacpp", LLAMA_CPP_BASE)

llm = llm_factory.get_llm("llamacpp","/mnt/storage/RandomCS/Models/LLM/models/tinyllama-1.1b-1t-Q4gguf/tinyllama-1.1b-intermediate-step-480k-1t.Q4_K_S.gguf", gpu_layers=100, context_length=2048)

def generate_reply(prompt: str, temperature = 0.4, use_template = True) -> str:
    return llm.generate(prompt, temperature = temperature, use_template = use_template)

# print(llm.generate(f"Given to you is a document.\n{qpr_data}Summarize the critical details of this document into listed points. All the details are to be taken from the document only.", use_template=True, temperature = 0.4))
# print(llm.generate(f"Given to you is a document.\n{qpr_data}What tag/label will you give this document so that user can identify what this document is about?", use_template=True, temperature = 0.4))
# print(llm.generate(f"How are you doing today?", use_template=True))
