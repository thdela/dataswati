FROM python:3.10-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir gradio scikit-learn pandas
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["python", "app.py"]
