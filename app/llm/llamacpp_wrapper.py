from llama_cpp import Llama
from llm.llm_blueprint import LLM_BASE
import template


class LLAMA_CPP_BASE(LLM_BASE):
    def __init__(
        self,
        path_to_model,
        gpu_layers=100,
        context_length=4096,
        seed=-1,
        n_threads=16,
        n_parts=-1,
    ):
        self.model = Llama(
            path_to_model,
            n_gpu_layers=gpu_layers,
            n_ctx=context_length,
            seed=seed,
            n_threads=n_threads,
            n_parts=n_parts,
            rope_freq_base=0,
            rope_freq_scale=0
        )

    def templify(self, prompt: str) -> str:
        """
        templify the prompt
        """

        template_file = open("llm/templates/inkbot_template.txt", "r") # Will change to automatically identify the file
        template = template_file.read()
        template = template.format(user_context = prompt)
        return template



    def generate(self, prompt, temperature=0.5, use_template=True):
        prompt = (
            self.templify(prompt=prompt)
            if use_template
            else prompt
        )
        stream_of_reply = self.model(
            prompt,
            stop=["Varoo"],
            max_tokens=8000,
            stream=True,
            temperature=temperature,
            top_k=0,
            top_p=0.73,
            # repeat_penalty=2
        )
        # print(prompt)

        reply = ""
        for line in stream_of_reply:
            reply += line["choices"][0]["text"]
            print(line["choices"][0]["text"], end = "", flush = True)

        return reply
