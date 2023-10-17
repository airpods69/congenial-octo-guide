from llm.llm_blueprint import LLMFactory
from llm.ctransformer_wrapper import CTRANSFORMERS_LLM

llm_factory = LLMFactory()
llm_factory.register_type("ctransformer", CTRANSFORMERS_LLM)

llm = llm_factory.get_llm("ctransformer", "TheBloke/Mistral-7B-v0.1-GGUF")

print(llm.generate("Hey there, how are you?", use_template=False))
