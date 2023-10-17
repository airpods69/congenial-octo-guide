from llm.llm_blueprint import LLM_BASE
import llm.template as template

from ctransformers import AutoModelForCausalLM


class CTRANSFORMERS_LLM(LLM_BASE):
    def __init__(self, model_name, gpu_layers) -> None:
        super().__init__()
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name, gpu_layers=gpu_layers, context_length=4000
        )

    def with_template(self, prompt: str) -> str:
        """
        Templifies the prompt, ie just wraps it around a template.
        """
        template_base = template.template
        chat_script = template.chat_script + prompt + "\n"

        return template_base + chat_script

        pass

    def without_template(self, prompt: str) -> str:
        """
        Returns the prompt as it is
        Input: Prompt
        Output: Prompt
        """
        return prompt

    def generate(self, prompt, max_new_tokens=4000, temperature=0.5, use_template=True):
        """
        Infer the LLM here
        """

        prompt = (
            self.with_template(prompt)
            if use_template
            else self.without_template(prompt)
        )

        reply = self.model(prompt, max_new_tokens=max_new_tokens, stop="User: ")

        return reply
