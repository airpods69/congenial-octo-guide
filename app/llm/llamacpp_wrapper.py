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
        )

    def templify(self, prompt: str, chat_script: str) -> str:
        """
        templify the prompt
        """
        USER_NAME = template.USER_NAME
        temp_base = template.template
        # chat_script = template.chat_script
        user_prompt = f"{USER_NAME}: {prompt}\n"
        print(chat_script)
        prompt = temp_base + chat_script
        prompt += user_prompt

        return prompt

    def generate(self, prompt, chat_script: str, temperature=0.5, use_template=True):
        prompt = (
            self.templify(prompt=prompt, chat_script=chat_script)
            if use_template
            else prompt
        )
        stream_of_reply = self.model(
            prompt,
            stop=[f"{template.USER_NAME}"],
            max_tokens=4000,
            stream=True,
            temperature=temperature,
            top_k=0,
            top_p=0.73,
        )
        # print(prompt)

        reply = ""
        for line in stream_of_reply:
            reply += line["choices"][0]["text"]

        return reply
