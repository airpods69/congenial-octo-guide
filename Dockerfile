FROM python:3.12.0

RUN pip3 install transformers ctransformers ctransformers[cuda]

CMD ["nvidia-smi"]
