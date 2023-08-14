FROM python:3.12.0b4-slim

WORKDIR  /adp

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN ln -sf /dev/stdout /adp/record.log

CMD [ "python", "handlers/webapp.py" ]

