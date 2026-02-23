FROM node:16-alpine

ENV BACKEND_URL=http://127.0.0.1:8000/api

ADD . /app/frontend

WORKDIR /app/frontend

RUN npm install

ENTRYPOINT [ "npm" ]

CMD [ "start" ]