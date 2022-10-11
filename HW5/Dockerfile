#FROM python:3.9.12-slim

FROM svizor/zoomcamp-model:3.9.12-slim
RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["q6predict.py", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen=localhost:9696 ", "q6predict:app"]