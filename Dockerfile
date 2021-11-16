FROM python:3.9.7

WORKDIR /usr/app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade pip 
RUN pip install -r requirements.txt 


COPY ./src/env_practice.py .


RUN mkdir result

CMD ["src/env_practice.py"]

ENTRYPOINT ["python3"]

