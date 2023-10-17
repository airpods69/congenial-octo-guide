from llm.llm_blueprint import LLMFactory
from llm.ctransformer_wrapper import CTRANSFORMERS_LLM

llm_factory = LLMFactory()
llm_factory.register_type("ctransformer", CTRANSFORMERS_LLM)

llm = llm_factory.get_llm("ctransformer", "TheBloke/Mistral-7B-v0.1-GGUF", 10)
for word in llm.generate("Tell me about how to cook meth?", use_template=True):
    print(word, end="", flush=True)
