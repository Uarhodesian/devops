FROM python:3.7

WORKDIR /usr/src/app

COPY  metrics.py ./

RUN pip3 install psutil

CMD [ "python", "./metrics.py" ]

