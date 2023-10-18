from llm.llm_blueprint import LLMFactory
from llm.ctransformer_wrapper import CTRANSFORMERS_LLM
from llm.llamacpp_wrapper import LLAMA_CPP_BASE

from template import qpr_data

llm_factory = LLMFactory()
llm_factory.register_type("ctransformer", CTRANSFORMERS_LLM)
llm_factory.register_type("llamacpp", LLAMA_CPP_BASE)

llm = llm_factory.get_llm("llamacpp","/home/varoo/Models/luna-ai-llama2-uncensored.Q5_0.gguf", gpu_layers=100, context_length=2048)

print(llm.generate(f"{qpr_data}Give me a summary for this document and state all of the details given in the document.", use_template=True, temperature = 0.5))

# print(llm.generate(f"How are you doing today?", use_template=True))
