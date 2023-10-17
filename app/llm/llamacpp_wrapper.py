from llama_cpp import Llama
from llm.llm_blueprint import LLM_BASE


class LLAMA_CPP_BASE(LLM_BASE):
    def __init__(
        self,
        path_to_model,
        gpu_layers = 100,
        context_length = 1024,
        seed=-1,
        n_threads=16,
        n_parts=-1,
    ):
        self.model = Llama(
            path_to_model,
            n_gpu_layers= gpu_layers,
            n_ctx = context_length,
            seed=seed,
            n_threads=n_threads,
            n_parts=n_parts,
        )

    def templify(self, prompt: str, template = None) -> str:
        """
        templify the prompt
        """
        if template == None:
            with open("./llm/templates/tinyllama.txt", "r") as f:
                template = "\n".join(f.readlines())

        prompt = template[:-1] + " " + prompt + "\n<|im_end|>\n<|im_start|>assistant"

        return prompt

    def generate(
        self, prompt, temperature=0.10, use_template = True
        ):
        stream_of_reply = self.model(
            prompt,
            stop=["<|im_start|>"],
            max_tokens=4096,
            stream=True,
            temperature=temperature,
        )
        prompt = self.templify(prompt = prompt) if use_template else prompt
        print(prompt)

        reply = ""
        for line in stream_of_reply:
            reply += line["choices"][0]["text"]

        return reply
