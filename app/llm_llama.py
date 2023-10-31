import template
from llama_cpp import Llama, LlamaRAMCache


class LLAMA:
    def __init__(
        self, model_path, n_gpu_layers=25, n_ctx=2048, seed=-1, n_threads=16, n_parts=-1
    ):
        print(
            "============= HELLO FROM LLAMA MODULE ==================\n {} is the model loaded".format(
                model_path
            )
        )
        self.llm = Llama(
            model_path,
            n_gpu_layers=n_gpu_layers,
            n_ctx=n_ctx,
            seed=seed,
            n_threads=n_threads,
            n_parts=n_parts,
        )
        self.USER_NAME = template.USER_NAME
        self.AI_NAME = template.AI_NAME
        self.template = template.template
        self.chat_script = template.chat_script

    def generate_reply(
        self, prompt, chat_script, guard_rails=True, internet_access=True
    ):
        old_chat_script = chat_script

        user_prompt = f"{self.USER_NAME}: {prompt}" + "\n"
        chat_script += user_prompt

        print(user_prompt)

        knowledge = ""

        print(f"Knowledge: {knowledge}")

        answer_stream = self.llm(
            "{}\n{}\n{}".format(self.template, knowledge, chat_script),
            stop=[f"{self.USER_NAME}"],
            max_tokens=2048,
            stream=True,
            temperature=0.72,
            top_k=0,
            top_p=0.73,
        )
        answer = ""

        for line in answer_stream:
            answer += line["choices"][0]["text"]

        print(answer)

        chat_script += f"{answer}" + "\n"
        chat_script = "\n".join(chat_script.split("\n")[2:])
        # print(self.chat_script.split("\n"))

        try:
            answer = answer.replace("  ", " ").split(f"{self.AI_NAME}:")[1]
        except Exception as e:
            answer = "I couldn't understand, try using a different prompt."
            chat_script = old_chat_script
            print(e)
        return answer, chat_script


def main():
    obj = LLAMA(
        model_path="/mnt/storage/RandomCS/text-generation-webui/models/tinyllama-1.1b-1t-Q4gguf/tinyllama-1.1b-intermediate-step-480k-1t.Q4_K_S.gguf"
    )
    print("---------------------------------------------------------")
    print(
        obj.generate_reply(
            f"{template.data}. Based on the given form details, who's signature is on signed this?",
            chat_script=template.chat_script,
        )
    )

    # print("---------------------------------------------------------")
    # obj.generate_reply("Oh what is the use of Anesthesia Machine? Can we kill someone with it? ")


if __name__ == "__main__":
    main()
