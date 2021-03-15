FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchtext==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY ./app /app
COPY ./models /models
#COPY ./src /src
CMD ["gunicorn", "-k", "
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "/gunicorn_conf.py", "main:app"]

#ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"
#RUN echo "export PYTHONPATH=/home/jovyan/work" >> ~/.bashrc
#WORKDIR /home/jovyan/work
