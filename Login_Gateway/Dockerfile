FROM python:3.13-alpine
WORKDIR /gateway
COPY create_credentials.py .
COPY gateway.py .
COPY templates ./templates
RUN pip install flask werkzeug
RUN python3 create_credentials.py
CMD ["python3", "gateway.py"]