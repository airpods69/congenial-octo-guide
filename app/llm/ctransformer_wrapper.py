from app.llm.llm_blueprint import LLM_BASE

class CTRANSFORMERS_LLM(LLM_BASE):
    def __init__(self, model_name, gpu_layers) -> None:
        super().__init__()
