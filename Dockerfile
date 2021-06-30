
FROM continuumio/miniconda3:4.9.2

ARG compile_cores=1

RUN apt-get --yes update && apt-get --yes upgrade

RUN apt-get install -y libgl1-mesa-glx libgl1-mesa-dev libglu1-mesa-dev \
                       freeglut3-dev libosmesa6 libosmesa6-dev \
                       libgles2-mesa-dev curl && \
                       apt-get clean

RUN conda install -c conda-forge -c python python=3.8 && \
    conda install -c conda-forge -c cadquery cadquery=2.1 && \
    pip install jupyter-cadquery==2.1.0 && \
    # change to clone repo and pip install locally
    pip install paramak && \
    conda clean -afy

COPY run_tests.sh run_tests.sh
COPY tests tests/

COPY example_python_package example_python_package/
COPY setup.py setup.py

RUN python setup.py install