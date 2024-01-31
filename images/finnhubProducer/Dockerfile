FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN mkdir -p /usr/local/share/ca-certificates/Yandex && wget "https://storage.yandexcloud.net/cloud-certs/CA.pem" --output-document /usr/local/share/ca-certificates/Yandex/YandexInternalRootCA.crt && chmod 0655 /usr/local/share/ca-certificates/Yandex/YandexInternalRootCA.crt

CMD ["python","src/finnhubProducer.py"]
