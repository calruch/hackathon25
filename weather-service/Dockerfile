FROM python:3.13-alpine
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY service.py config.py ./
COPY templates ./templates

# Default environment values (override via docker run -e ...)
ENV SECRET_KEY=Gandalf_the_White
ENV PORT=5001
ENV WEATHER_FORMAT=3

EXPOSE 5001
CMD ["python", "service.py"]