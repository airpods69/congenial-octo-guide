FROM nvidia/cuda:11.7.1-devel-ubuntu22.04

WORKDIR /code
ENV DEBIAN_FRONTEND noninteractive
ENV FLASK_APP=llm_backend.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apt update && apt install git -y
RUN apt install python3-pip -y
RUN apt install ffmpeg libsm6 libxext6 -y
# RUN MINICONDA="Miniconda3-latest-Linux-x86_64.sh" && \
#     wget --quiet https://repo.continuum.io/miniconda/$MINICONDA && \
#     bash $MINICONDA -b -p /miniconda && \
#     rm -f $MINICONDA && \
#     echo ". /miniconda/etc/profile.d/conda.sh" >> ~/.bashrc
# ENV PATH /miniconda/bin:$PATH

RUN CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir --user

COPY requirements.txt requirements.txt

# RUN conda update -n base conda
RUN pip install -r requirements.txt
# RUN conda activate base

COPY . .

CMD ["python3", "llm_interface.py"]
