FROM python:3.13-alpine
WORKDIR /service
COPY service.py .
COPY templates ./templates
RUN pip install flask requests
CMD ["python", "service.py"]