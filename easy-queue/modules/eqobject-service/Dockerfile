FROM continuumio/miniconda:latest

WORKDIR /home/app

COPY environment.yml ./
COPY *.txt ./
COPY *.md ./
COPY eqobject/ ./eqobject/
COPY docker-entrypoint.sh ./

RUN chmod +x docker-entrypoint.sh
RUN conda update conda
RUN conda env create -f environment.yml

RUN echo "source activate easy-queue" > ~/.bashrc
ENV PATH /opt/conda/envs/easy-queue/bin:$PATH

EXPOSE 15000

ENTRYPOINT ["./docker-entrypoint.sh"]
#ENTRYPOINT ["/bin/sh"]