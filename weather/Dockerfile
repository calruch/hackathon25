FROM python:3.13-alpine
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY service.py .
COPY config.py .

ENV SECRET_KEY=Gandalf_the_White
ENV PORT=5001
ENV WEATHER_FORMAT=3

CMD ["python", "service.py"]