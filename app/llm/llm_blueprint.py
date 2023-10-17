"""
Blueprint of LLM architecture
"""

from abc import ABC, abstractmethod


class LLM_BASE(ABC):
    @abstractmethod
    def generate(self, prompt, temperature):
        pass


class LLMFactory:
    def __init__(self):
        self._creatores = {}

    def register_type(self, key, creator):
        self._creatores[key] = creator

    def get_llm(self, key, path_to_model, gpu_layers):
        creator = self._creatores[key]
        if not creator:
            raise ValueError("Unsupported LLM Engine Type")
        return creator(path_to_model, gpu_layers)
