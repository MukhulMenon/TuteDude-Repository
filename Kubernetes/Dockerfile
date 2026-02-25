FROM python:3.9-alpine

WORKDIR /app

ADD . .

RUN pip install -r test-app/requirements.txt

ENTRYPOINT [ "python" ]

CMD ["test-app/app.py" ]