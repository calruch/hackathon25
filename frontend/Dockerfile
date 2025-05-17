FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x create_credentials.py
EXPOSE 5000
ENTRYPOINT ["sh", "-c", "python create_credentials.py && python app.py"]
