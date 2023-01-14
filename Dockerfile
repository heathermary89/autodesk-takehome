FROM python:3.8

WORKDIR  /adp

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "handlers/webapp.py" ]

