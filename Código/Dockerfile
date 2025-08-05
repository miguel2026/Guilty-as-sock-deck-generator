FROM python:3.12-alpine3.21
WORKDIR /Código
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:API","--host","0.0.0.0", "--reload"]