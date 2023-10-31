from llm.llm_blueprint import LLMFactory
from llm.ctransformer_wrapper import CTRANSFORMERS_LLM
from llm.llamacpp_wrapper import LLAMA_CPP_BASE
from template import qpr_data

llm_factory = LLMFactory()
llm_factory.register_type("ctransformer", CTRANSFORMERS_LLM)
llm_factory.register_type("llamacpp", LLAMA_CPP_BASE)

llm = llm_factory.get_llm(
    "llamacpp",
    "/home/varoo/Models/inkbot-13b-8k-0.2.Q5_K_M.gguf",
    gpu_layers=100,
    context_length=8000,
)


def generate_reply(
    prompt: str, temperature=0.2, use_template=True
) -> str:
    return llm.generate(
        prompt, temperature=temperature, use_template=use_template
    )

prompt = f"{qpr_data}"

print(llm.generate(f"{prompt}", use_template=True, temperature = 0.3))
# print(llm.generate(f"Given to you is a document.\n{qpr_data}What tag/label will you give this document so that user can identify what this document is about?", use_template=True, temperature = 0.4))
# print(llm.generate(f"How are you doing today?", use_template=True))
