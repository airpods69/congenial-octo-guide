from llama_cpp import Llama
from llm.llm_blueprint import LLM_BASE


class LlamacppBase(LLM_BASE):
    def __init__(
        self,
        path_to_model,
        n_gpu_layers=100,
        n_ctx=1024,
        seed=-1,
        n_threads=16,
        n_parts=-1,
    ):
        self.model = Llama(
            path_to_model,
            n_gpu_layers=n_gpu_layers,
            n_ctx=n_ctx,
            seed=seed,
            n_threads=n_threads,
            n_parts=n_parts,
        )

    def inference(
        self, prompt, stop_words=["\n"], temperature=0.72, top_k=0, top_p=0.73
    ):
        stream_of_reply = self.model(
            prompt,
            stop=stop_words,
            max_tokens=4096,
            stream=True,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
        )

        reply = ""
        for line in stream_of_reply:
            reply += line["choices"][0]["text"]

        return reply
