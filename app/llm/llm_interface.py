from llm.llm_blueprint import LLMFactory
from llm.ctransformer_wrapper import CTRANSFORMERS_LLM
from llm.llamacpp_wrapper import LLAMA_CPP_BASE

llm_factory = LLMFactory()
llm_factory.register_type("ctransformer", CTRANSFORMERS_LLM)
llm_factory.register_type("llamacpp", LLAMA_CPP_BASE)

llm = llm_factory.get_llm(
    "llamacpp",
    "/mnt/storage/RandomCS/text-generation-webui/models/tinyllama-1.1b-1t-Q4gguf/tinyllama-1.1b-intermediate-step-480k-1t.Q4_K_S.gguf",
    gpu_layers=20,
    context_length=4000,
)

print(llm.generate("who are you?", use_template=False))
